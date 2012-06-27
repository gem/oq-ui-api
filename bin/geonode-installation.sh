#!/bin/bash
# set -x

# Version: 0.4.0-isc_viewer (isc_viewer branch)
# Guidelines
#
#    Configuration file manglings are done only if they not appear already made.
#

#
# PUBLIC GLOBAL VARS
# version managements - use "master" or tagname to move to other versions
export GEM_DJANGO_SCHEMATA_GIT_REPO=git://github.com/tuttle/django-schemata.git
export GEM_DJANGO_SCHEMATA_GIT_VERS=8f9487b70c9b1508ae70b502b950066147956993

export       GEM_OQ_UI_API_GIT_REPO=git://github.com/gem/oq-ui-api.git
export       GEM_OQ_UI_API_GIT_VERS=tom2apa-clients

export    GEM_OQ_UI_CLIENT_GIT_REPO=git://github.com/gem/oq-ui-client.git
export    GEM_OQ_UI_CLIENT_GIT_VERS=tom2apa-clients

export GEM_OQ_UI_GEOSERVER_GIT_REPO=git://github.com/gem/oq-ui-geoserver.git
export GEM_OQ_UI_GEOSERVER_GIT_VERS=v0.4.0

export GEM_DB_NAME="geonode_dev"

#
# PRIVATE GLOBAL VARS
export GEM_DB_USER="geonode"
export GEM_POSTGIS_PATH=/usr/share/postgresql/8.4/contrib/postgis-1.5
export GEM_HOSTNAME="$(hostname)"
export GEM_TMPDIR="gem_tmp"
export GEM_BASEDIR="/var/lib/openquake"
export GEM_GN_LOCSET="/etc/geonode/local_settings.py"
export GEM_GN_SETTINGS="/var/lib/geonode/src/GeoNodePy/geonode/settings.py"
export GEM_GN_URLS="/var/lib/geonode/src/GeoNodePy/geonode/urls.py"
export GEM_NW_SETTINGS="/etc/geonode/geonetwork/config.xml"
export GEM_TOMCAT_LOGFILE="/var/log/geonode/tomcat.log"
export GEM_WSGI_CONFIG="/var/www/geonode/wsgi/geonode.wsgi"
export NL='
'
export TB='	'

#
# FUNCTIONS
usage () {
    local name err
    
    name="$1"
    err="$2"
    echo "Usage:"
    echo "  $name"
    echo "  Run the command from your normal user account"
    echo
    echo "  $name <-s|--setgit>"
    echo "  Set current git repo and commit into oq_ui_api script variables"
    echo
    echo "  $name <-h|--help>"
    echo "  This help"
    echo 
    exit $err
}

# tomcat_wait_start is a function that check if the tomcat daemon complete it's boot
# looking inside it's log file searching the "INFO: Server startup" line
tomcat_wait_start () {
    local tws_i log_cur every nloop

    log_cur=$1
    every=$2
    nloop=$3

    for tws_i in $(seq 1 $nloop); do
        tail -n +$log_cur $GEM_TOMCAT_LOGFILE | grep -q "^INFO: Server startup "
        if [ $? -eq 0 ]; then
            return 0
        fi
        sleep $every
    done
    return 1
    }

# this function create a required directory. if fails the script exits with error level 2
# with '-d' flag try to remove the dir before creation
mkreqdir () {
    local d

    if [ $# -gt 1 -a "$1" = "-d" ]; then
        rm -rf "$2"
        shift
    fi
    d="$1"

    if [ ! -d "$d" ]; then
        mkdir -p "$d"
    fi

    if [ ! -d "$d" ]; then
        echo "ERROR: '$d' dir creation failed" 
        exit 2
    fi
    return 0
}

schemata_config_add() {
    local sche_dom sche_domn sche_name

    sche_domn="$1"
    sche_name="$2"

    sche_dom="$(sed -n '/^SCHEMATA_DOMAINS *=/,/^}$/p' "$GEM_GN_LOCSET" | tail -n +2 | tr -d '\n' | sed 's/},/},\n/g')"
    echo "$sche_dom" | grep -q "^[ 	]*'$sche_domn':[ 	]*{[ 	]*'schema_name':[ 	]*'$sche_name',[ 	]*}"
    if [ $? -ne 0 ]; then
        sed -i "s/^\(SCHEMATA_DOMAINS *= *.*\)/\1\n  '$sche_domn': {\n    'schema_name': '$sche_name',\n    },\n/g" "$GEM_GN_LOCSET"
    else
        echo "WARNING: $sche_domn just exists into SCHEMATA_DOMAINS entry of $GEM_GN_LOCSET"
        echo "$sche_dom"
        read -p "If it isn't correct, edit it and continue" a            
    fi
}

installed_apps_add() {
    local new_app inst_apps

    new_app="$1"

    inst_apps="$(sed -n '/^INSTALLED_APPS[ 	]*=[ 	]*/,/)/p' "$GEM_GN_SETTINGS")"
    echo "$inst_apps" | grep -q "'$new_app'"
    if [ $? -ne 0 ]; then
        sed -i "s/^\(INSTALLED_APPS[ 	]*=[ 	]*.*\)/\1\n    '$new_app',/g"   "$GEM_GN_SETTINGS"
    fi
}
##
# verify host distro compatibility
check_distro () {
    local distro rel
    dpkg -l lsb-release | grep -q 'ii[ 	]*lsb-release[ 	]*' >/dev/null 2>&1
    if [ $? -ne 0 ]; then
        apt-get install -y lsb-release >/dev/null 2>&1
        if [ $? -ne 0 ]; then
            echo " lsb-release installation failed" 
            return 2
        fi
    fi
    distro="$(lsb_release -i | sed 's/^Distributor ID:[ 	]*//g')"     
    rel="$(lsb_release -r  | sed 's/^Release:[ 	]*//g')" 
    if [ "$distro" != "Ubuntu" ]; then
        return 2
    elif [ "$rel" != "10.10" -a "$rel" != "11.04" ]; then
        return 1
    fi
    return 0
}

    
apache_append_proxy () {
    local pa

    pa="$1"
    grep -q "$pa" /etc/apache2/sites-available/geonode
    if [ $? -ne 0 ]; then
        sed -i "s@\(</VirtualHost>.*\)@$pa\n\1@g" /etc/apache2/sites-available/geonode
    fi
}

geonode_installation () { 
    local norm_user norm_dir ret a distdesc
    local cur_step

    cur_step=0

    norm_user="$1"
    norm_dir="$2"

    ###
    # Verify if the distribution is compliant with the script.
    check_distro
    ret=$?
    distdesc=" $(lsb_release  -d | sed 's/Description:[ 	]*//g')" 
    if [ $ret -eq 1 ]; then
        echo "WARNING: this script is designed to run on Ubuntu 10.10 and 11.04, not on ${distdesc}."
        read -p "press ENTER to continue AT YOUR OWN RISK or CTRL+C to abort." a
    elif [ $ret -eq 2 ]; then
        echo "ERROR: ${distdesc} not supported" 
        exit 1
    fi

    # Get public name info
    defa="$GEM_HOSTNAME"
    read -p "Public site url or public IP address [$defa]: " SITE_HOST
    if [ "$SITE_HOST" = "" ]; then
        SITE_HOST="$defa"
    fi
    export SITE_HOST

    mkreqdir "$GEM_TMPDIR"
    rm -rf "$GEM_TMPDIR"/*

    mkreqdir "$GEM_BASEDIR"
    
    ###
    echo "== General requirements ==" 
    apt-get install -y python-software-properties
    add-apt-repository ppa:geonode/release
    apt-add-repository ppa:openquake/ppa
    apt-get update

    apt-get install -y git ant openjdk-6-jdk make python-lxml python-jpype python-newt python-shapely libopenshalite-java

    ###
    echo "== Geonode installation ==" 
    # moved at the top of the function 
    # defa="$GEM_HOSTNAME"
    # read -p "Public site url or public IP address [$defa]: " SITE_HOST
    # if [ "$SITE_HOST" = "" ]; then
    #     SITE_HOST="$defa"
    # fi
    # export SITE_HOST

#
# NOTE: this part was used to change the apt geonode repository
#
#    if [ -f /etc/apt/sources.list.d/geonode-release-maverick.list ]; then
#        mv /etc/apt/sources.list.d/geonode-release-maverick.list /etc/apt/sources.list.d/geonode-release-natty.list
#        sed -i 's/maverick/natty/g' /etc/apt/sources.list.d/geonode-release-natty.list
#    else
#        echo "add-apt-repository ppa:geonode/release command failed"
#        echo "installation ABORTED"
#        exit 1
#    fi  
    gem_oldpath="$PATH"
    export PATH=/usr/lib/python-django/bin:$PATH
    export VIRTUALENV_SYSTEM_SITE_PACKAGES=true
    apt-get install -y geonode
    
    sed -i "s@^ *SITEURL *=.*@SITEURL = 'http://$SITE_HOST/'@g" "$GEM_GN_LOCSET"
    grep -q '^WSGIDaemonProcess.*:/var/lib/geonode/src/GeoNodePy/geonode' /etc/apache2/sites-available/geonode 
    if [ $? -ne 0 ]; then
        sed -i 's@\(^WSGIDaemonProcess.*$\)@\1:/var/lib/geonode/src/GeoNodePy/geonode@g' /etc/apache2/sites-available/geonode
    fi
    cat /etc/apache2/sites-enabled/geonode | grep -v '^[ 	]*Alias /oq-platform/ ' | \
        sed 's@\(\(^[ 	]*Alias \)/static/ /var/www/geonode/static/\)@\1\n\2/oq-platform/ /var/lib/openquake/oq-ui-client/oq-platform/@g' >/etc/apache2/sites-enabled/geonode

    # this fix the bug 972202 to inform jpype module where is the java installation
    sed -i "s@os.environ\['DJANGO_SETTINGS_MODULE'\] *= *'geonode.settings'@os.environ['DJANGO_SETTINGS_MODULE'] = 'geonode.settings'\nos.environ['JAVA_HOME'] = '/usr/lib/jvm/java-6-openjdk'@g" "$GEM_WSGI_CONFIG"

    service tomcat6 restart
    service apache2 restart
    wget --save-headers -O "$GEM_TMPDIR/test_geonode.html" "http://$SITE_HOST/"

    head -n 1 "$GEM_TMPDIR/test_geonode.html" > "$GEM_TMPDIR/test_geonode.http"
    grep -q 200 "$GEM_TMPDIR/test_geonode.http"
    if [ $? -ne 0 ]; then
        echo 
        echo "WARNING: GEONODE WEB TEST FAILED!"
        cat test_geonode.http
        echo
        read -p "press ENTER to continue or CTRL+C to abort:" a
    fi

    ###
    echo "== Django-South and Django-Schemata installation =="
        
    sudo su - $norm_user -c "
cd $norm_dir
git clone $GEM_DJANGO_SCHEMATA_GIT_REPO
"
    mkreqdir -d "$GEM_BASEDIR"/django-schemata
    cd django-schemata
    git archive $GEM_DJANGO_SCHEMATA_GIT_VERS | tar -x -C "$GEM_BASEDIR"/django-schemata
    ln -s "$GEM_BASEDIR"/django-schemata/django_schemata /var/lib/geonode/src/GeoNodePy/geonode
    cd -
    apt-get install -y python-django-south

    ###
    echo "== Django-South configuration =="

    ##
    #    /var/lib/geonode/src/GeoNodePy/geonode/settings.py
    midd_class="$(sed -n '/^MIDDLEWARE_CLASSES[ 	]*=[ 	]*/,/)/p' "$GEM_GN_SETTINGS")"

    echo "$midd_class=" | grep -q "'django_schemata\.middleware\.SchemataMiddleware'" 
    if [ $? -ne 0 ]; then
        sed -i "s/^\(MIDDLEWARE_CLASSES *= *.*\)/\1\n    'django_schemata.middleware.SchemataMiddleware',/g" "$GEM_GN_SETTINGS"
    fi

    installed_apps_add 'south'
    installed_apps_add 'django_schemata'

    ##
    # /etc/geonode/local_settings.py
    grep -q "^[ 	]*'ENGINE':.*" "$GEM_GN_LOCSET"
    if [ $? -ne 0 ]; then
        echo "Required 'ENGINE' entry into $GEM_GN_LOCSET not found"
        exit 3
    fi
    sed -i "s/^\([ 	]*'ENGINE':\)\(.*\)/# \1\2\n\1 'django_schemata.postgresql_backend',/g" "$GEM_GN_LOCSET"

    grep -q 'SCHEMATA_DOMAINS[ 	]*=[ 	]*' "$GEM_GN_LOCSET"
    if [ $? -ne 0 ]; then
        echo "\
SCHEMATA_DOMAINS = { 
  '$SITE_HOST': {
    'schema_name': 'gem',
    }
  }" >> "$GEM_GN_LOCSET"
    else
        schemata_config_add "$SITE_HOST" "gem"
    fi

    grep -q '^SOUTH_DATABASE_ADAPTERS[ 	]*=[ 	]*' "$GEM_GN_LOCSET"
    if [ $? -ne 0 ]; then
        echo "\
SOUTH_DATABASE_ADAPTERS = { 
    'default': 'south.db.postgresql_psycopg2',
}" >> "$GEM_GN_LOCSET"
    fi

    ###
    echo "== Database recreation ==" 
    
    service apache2 stop 
    service tomcat6 stop

    sudo su - postgres -c "
dropdb $GEM_DB_NAME || true
createdb -O $GEM_DB_USER $GEM_DB_NAME 
createlang plpgsql $GEM_DB_NAME 
psql -f $GEM_POSTGIS_PATH/postgis.sql $GEM_DB_NAME 
psql -f $GEM_POSTGIS_PATH/spatial_ref_sys.sql $GEM_DB_NAME 
"
    
    sed -i "s/DATABASE_NAME[ 	]*=[ 	]*'\([^']*\)'/DATABASE_NAME = '$GEM_DB_NAME'/g" "$GEM_GN_LOCSET"
    sed -i "s@\(<url>jdbc:postgresql:\)[^<]*@\1geonode_dev@g" "$GEM_NW_SETTINGS"

    service apache2 start
    service tomcat6 start

    postgis_vers="$(dpkg-query --show -f '${Version}' postgis 2>/dev/null)"
    if [ $? -ne 0 ]; then
        echo "Postgis not found, verify your system."
        exit 3
    fi
    postgis_vers="$(echo "$postgis_vers" | sed 's/-.*//g')"

    grep -q '^POSTGIS_VERSION[ 	]*=[ 	]*' "$GEM_GN_LOCSET"
    if [ $? -eq 0 ]; then
        sed -i "s/^\(POSTGIS_VERSION[ 	]*=[ 	]*['\"]\)[0-9\.]\+\(.*\)/\1$postgis_vers\2/g" "$GEM_GN_LOCSET"
    else
        echo "POSTGIS_VERSION = '$postgis_vers'" >> "$GEM_GN_LOCSET"
    fi

    grep -q '^ORIGINAL_BACKEND[ 	]*=[ 	]*' "$GEM_GN_LOCSET"
    if [ $? -eq 0 ]; then
        sed -i "s/^\(ORIGINAL_BACKEND[ 	]*=[ 	]*\)\(['\"]\).*/\1\2django.contrib.gis.db.backends.postgis\2/g" "$GEM_GN_LOCSET"
    else
        echo "ORIGINAL_BACKEND = 'django.contrib.gis.db.backends.postgis'" >> "$GEM_GN_LOCSET"
    fi

    grep -q '^GEOCLUDGE_JAR_PATH[ 	]*=[ 	]*' "$GEM_GN_LOCSET"
    if [ $? -eq 0 ]; then
        sed -i "s@^\(GEOCLUDGE_JAR_PATH[ 	]*=[ 	]*\)\(['\"]\).*@\1\2/usr/share/java\2@g" "$GEM_GN_LOCSET"
    else
        echo "GEOCLUDGE_JAR_PATH = '/usr/share/java'" >> "$GEM_GN_LOCSET"
    fi

    ###
    echo "== Add 'geodetic', 'ged4gem', 'observations' and 'isc_viewer' Django applications =="

    sudo su - $norm_user -c "
cd $norm_dir 
test ! -d oq-ui-api || rm -Ir oq-ui-api 
git clone $GEM_OQ_UI_API_GIT_REPO"
    cd oq-ui-api
    git checkout $GEM_OQ_UI_API_GIT_VERS
    make fix
    make MKREQDIR_ARG="-d" deploy
     
    ##
    # /etc/geonode/local_settings.py    
    schemata_config_add 'geodetic'      'geodetic'
    schemata_config_add 'django'        'public'
    schemata_config_add 'ged4gem'       'eqged'
    schemata_config_add 'isc_viewer'    'isc_viewer'

    ##
    # /var/lib/geonode/src/GeoNodePy/geonode/settings.py    
    installed_apps_add 'geonode.ged4gem'
    installed_apps_add 'geonode.observations'
    installed_apps_add 'geonode.geodetic'
    installed_apps_add 'geonode.isc_viewer'

    ## add observations to urls.py
    #     (r'^observations/', include('geonode.observations.urls')),
    sed -i "s@urlpatterns *= *patterns('',@urlpatterns = patterns('',\n    # added by geonode-installation.sh script\n    (r'^observations/', include('geonode.observations.urls')),@g" "$GEM_GN_URLS"


    ##
    # deploy database
    cd /var/lib/geonode/
    source bin/activate
    cd src/GeoNodePy/geonode/
    python ./manage.py manage_schemata
    export DJANGO_SCHEMATA_DOMAIN=django
    python ./manage.py syncdb
    export DJANGO_SCHEMATA_DOMAIN=geodetic
    python ./manage.py migrate geodetic
    export DJANGO_SCHEMATA_DOMAIN=isc_viewer
    python ./manage.py migrate isc_viewer
    if [ -f "$norm_dir/private_data/isc_data.csv" ]; then
        GEM_ISC_DATA="$norm_dir/private_data/isc_data.csv"
    else
        GEM_ISC_DATA="$norm_dir/oq-ui-api/data/isc_data.csv"
    fi
    python ./manage.py importcsv "$GEM_ISC_DATA"
    export DJANGO_SCHEMATA_DOMAIN="$SITE_HOST"
    python ./manage.py migrate observations
    export DJANGO_SCHEMATA_DOMAIN=ged4gem
    python ./manage.py migrate ged4gem

    cd $norm_dir

    ##
    echo "Add 'faultedearth', 'geodetic', 'isc_viewer', 'exposure_country' and 'exposure_grid' client applications"
    sudo su - $norm_user -c "
cd \"$norm_dir\"
test ! -d oq-ui-client || rm -Ir oq-ui-client
git clone $GEM_OQ_UI_CLIENT_GIT_REPO
cd oq-ui-client
git checkout $GEM_OQ_UI_CLIENT_GIT_VERS
git submodule init
git submodule update
ant init"

# ant debug -Dapp.port=8081 &
# debug_pid=\$!
# sleep 10
# kill -0 \$debug_pid
# if [ \$? -ne 0 ]; then
#     echo \"oq-ui-client checkpoint\"
#     echo \"ERROR: 'ant debug' failed\"
#     exit 4
# fi
# kill -TERM \$debug_pid
# exit 0
# "
    ret=$?
    if [ $ret -ne 0 ]; then
        exit $ret
    fi

    cd oq-ui-client
    ant deploy
if [ 0 -eq 1 ]; then    
    ## 
    # FaultedEarth 
    sudo su - $norm_user -c "
cd \"$norm_dir\"
cd oq-ui-client
sed -i 's@\(<project name=\"\)[^\"]*\(\" \)@\1FaultedEarth\2@g;s/^\( *\).*\(Build File.*\)$/\1FaultedEarth \2/g' build.xml
cp app/static/index_FE_fault.html app/static/index.html 
ant static-war
"
    cp oq-ui-client/build/FaultedEarth.war /var/lib/tomcat6/webapps/

    ##
    # geodetic
    sudo su - $norm_user -c "
cd \"$norm_dir\"
cd oq-ui-client
sed -i 's@\(<project name=\"\)[^\"]*\(\" \)@\1geodetic\2@g;s/^\( *\).*\(Build File.*\)$/\1geodetic \2/g' build.xml
cp app/static/index_geodetic.html app/static/index.html 
ant static-war
"
    cp oq-ui-client/build/geodetic.war /var/lib/tomcat6/webapps/
    ##
    # isc_viewer
    sudo su - $norm_user -c "
cd \"$norm_dir\"
cd oq-ui-client
sed -i 's@\(<project name=\"\)[^\"]*\(\" \)@\1isc_viewer\2@g;s/^\( *\).*\(Build File.*\)$/\1isc_viewer \2/g' build.xml
cp app/static/index_isc_viewer.html app/static/index.html
ant static-war
"
    cp oq-ui-client/build/isc_viewer.war /var/lib/tomcat6/webapps/

    ##
    # GED4GEM_country 
    sudo su - $norm_user -c "
cd \"$norm_dir\"
cd oq-ui-client
sed -i 's@\(<project name=\"\)[^\"]*\(\" \)@\1GED4GEM_country\2@g;s/^\( *\).*\(Build File.*\)$/\1GED4GEM_country \2/g' build.xml
cp app/static/index_GED_country.html app/static/index.html 
ant static-war
"
    cp oq-ui-client/build/GED4GEM_country.war /var/lib/tomcat6/webapps/

    ##
    # GED4GEM_Exposure
    sudo su - $norm_user -c "
cd \"$norm_dir\"
cd oq-ui-client
sed -i 's@\(<project name=\"\)[^\"]*\(\" \)@\1GED4GEM_Exposure\2@g;s/^\( *\).*\(Build File.*\)$/\1GED4GEM_Exposure \2/g' build.xml
cp app/static/index_GED_exposure.html app/static/index.html 
ant static-war
"
    cp oq-ui-client/build/GED4GEM_Exposure.war /var/lib/tomcat6/webapps/


    ##
    # configuration
    apache_append_proxy 'ProxyPass /FaultedEarth http://localhost:8080/FaultedEarth'
    apache_append_proxy 'ProxyPassReverse /FaultedEarth http://localhost:8080/FaultedEarth'
    apache_append_proxy 'ProxyPass /geodetic http://localhost:8080/geodetic'
    apache_append_proxy 'ProxyPassReverse /geodetic http://localhost:8080/geodetic'
    apache_append_proxy 'ProxyPass /isc_viewer http://localhost:8080/isc_viewer'
    apache_append_proxy 'ProxyPassReverse /isc_viewer http://localhost:8080/isc_viewer'
    apache_append_proxy 'ProxyPass /GED4GEM_country http://localhost:8080/GED4GEM_country'
    apache_append_proxy 'ProxyPassReverse /GED4GEM_country http://localhost:8080/GED4GEM_country'
    apache_append_proxy 'ProxyPass /GED4GEM_Exposure http://localhost:8080/GED4GEM_Exposure'
    apache_append_proxy 'ProxyPassReverse /GED4GEM_Exposure http://localhost:8080/GED4GEM_Exposure'
fi

    service tomcat6 restart
    service apache2 restart

    ###
    echo "== Custom geoserver installation =="

    service tomcat6 stop
    
    sudo su - $norm_user -c "
cd $norm_dir
test ! -d oq-ui-geoserver || rm -Ir oq-ui-geoserver
git clone $GEM_OQ_UI_GEOSERVER_GIT_REPO
cd oq-ui-geoserver
git checkout $GEM_OQ_UI_GEOSERVER_GIT_VERS
"
    mkreqdir -d "$GEM_BASEDIR"/oq-ui-geoserver
    cd oq-ui-geoserver
    make deploy
    if [ -d /var/lib/tomcat6/webapps/geoserver -a ! -L /var/lib/tomcat6/webapps/geoserver ]; then
        mv /var/lib/tomcat6/webapps/geoserver "$GEM_BASEDIR"/geoserver.orig
    fi

    ln -s "$GEM_BASEDIR"/oq-ui-geoserver/geoserver /var/lib/tomcat6/webapps/geoserver
    cd -

    ##
    # configuration
    if [ ! -f /var/lib/tomcat6/webapps/geoserver/WEB-INF/web.xml -o ! -f /etc/geonode/geoserver/web.xml ]; then
        echo "geoserver configuration file not found"
        return 6
    fi
    for conf_file in /var/lib/tomcat6/webapps/geoserver/WEB-INF/web.xml /etc/geonode/geoserver/web.xml; do
        fname="$(basename "$conf_file")"
        cat "$conf_file" | \
        sed -n '/^.*<param-name>GEONODE_BASE_URL<\/param-name>/{p;n;x;d};p'   | sed "s@^\( *\)\(<param-name>GEONODE_BASE_URL</param-name>.*\)@\1\2\n\1<param-value>http://$SITE_HOST/</param-value>@g" | \
        sed -n '/^.*<param-name>GEOSERVER_DATA_DIR<\/param-name>/{p;n;x;d};p' | sed "s@^\( *\)\(<param-name>GEOSERVER_DATA_DIR</param-name>.*\)@\1\2\n\1<param-value>/var/lib/tomcat6/webapps/geoserver/data/</param-value>@g" > $GEM_TMPDIR/${fname}.new
        cp $GEM_TMPDIR/${fname}.new "$conf_file"
    done

    tc_log_cur="$(cat /var/log/geonode/tomcat.log  | wc -l)"
    service tomcat6 start
    ##
    # final alignment

    # check if tomcat had finish it's startup (try every 5 secs for 24 times => 2 mins)
    tomcat_wait_start $tc_log_cur 5 24
    service apache2 restart
    sleep 20

    #
    #  NOTE: for some unknown reasons the last step fails the first time that we run.
    #        To not waste time to investigate this strage problem we use a "retry approach".
    #

    unset VIRTUALENV_SYSTEM_SITE_PACKAGES
    export PATH="$gem_oldpath"
    cd /var/lib/geonode/
    source bin/activate
    cd src/GeoNodePy/geonode/
    export DJANGO_SCHEMATA_DOMAIN="$SITE_HOST"
    for i in $(seq 1 5); do
	python ./manage.py updatelayers
	if [ $? -eq 0 ]; then
            break
        fi
        sleep 20
    done
    deactivate
    

#
#  THE END
#

    # echo "From root we have: norm_user: $norm_user  norm_dir: $norm_dir SITE_HOST: $SITE_HOST"
    return 0    
}



#
#  MAIN
#
wai="$(whoami)"
setgit=
#
#  args management
while [ $# -gt 0 ]; do
    case $1 in
        -s | --setgit)
            setgit=1
            shift            
            ;;
        *)
            break
            ;;
    esac
done

if [ $setgit ]; then
    echo "settato"
    git_commit="$(git log -1 --pretty=format:%H)"
    if [ $? -ne 0 ]; then
        echo "Git commit version not found"
        exit 1
    fi
    git_repos="$(git remote -v | grep "(fetch)$")"
    git_repos_n="$(echo "$git_repos" | wc -l)"

    if [ $git_repos_n -eq 1 ]; then
        git_repo="$(echo "$git_rems" | awk '{ printf("%s\n", $2); }')"
    else
        echo "More then 1 remote repository found:"
        while [ true ]; do
            IFS="$NL"
            ct=1
            for rem_item in $git_repos; do
                echo "$ct)${TB}$rem_item"
                ct=$((ct + 1))
            done
            read -p "Choose (1 - $git_repos_n): " ch
            echo "$ch" | grep -q '^[-+]\?[0-9]\+$'
            if [ $? -ne 0 ]; then
                continue
            fi
            if [ "$ch" -ge 1 -a "$ch" -le $git_repos_n ]; then
                break
            fi
        done
        IFS='$NL	 '
        git_repo="$(echo "$git_repos" | tail -n +$ch | head -n 1 | awk '{ printf("%s\n", $2); }' )"
        
        echo "GIT_REPO:   $git_repo"
        echo "GIT_COMMIT: $git_commit"

        sed -i "s|^\(export[ 	]\+GEM_OQ_UI_API_GIT_REPO=\).*|\1$git_repo|g;s|^\(export[ 	]\+GEM_OQ_UI_API_GIT_VERS=\).*|\1$git_commit|g" $0 
    fi
    exit 0
fi

if [ "$wai" = "root" ]; then
    if [ $# -eq 2 ]; then
        norm_user="$1"
        norm_dir="$2"
        
        geonode_installation "$norm_user" "$norm_dir"
        exit $?
    else
        usage "$0" 1
    fi
elif [ $# -eq 0 ]; then
    echo "You are running the geonode installation script."
    echo
    echo "During this operation some git repositories will be downloaded into the current"
    echo "directory $PWD."
    echo
    read -p "press ENTER to continue or CTRL+C to abort:" a
    echo 
    sudo -p "To install geonode root permissions are needed.${NL}Please type password for $wai: " $0 "$wai" "$PWD"
    exit $?
else
    usage "$0" 1
fi

