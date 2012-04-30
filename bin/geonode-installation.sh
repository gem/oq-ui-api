#!/bin/bash
# set -x

# Guidelines
#
#    Configuration file manglings are done only if they not appear already made.
#

#
# PUBLIC GLOBAL VARS
# version managements - use "master" or tagname to move to other versions
export GEM_DJANGO_SCHEMATA_GIT_VERS=8f9487b70c9b1508ae70b502b950066147956993
export       GEM_OQ_UI_API_GIT_VERS=fc689867330f78c883d1283a2542bdba12835083
export    GEM_OQ_UI_CLIENT_GIT_VERS=2224d2eff6ca5ec8de33372a40a1c7fccaa0469f
export GEM_OQ_UI_GEOSERVER_GIT_VERS=fbe1f48f1e40dd91e1e2dfcad5bebaf20a208b1e
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
export NL='
'

#
# FUNCTIONS
usage () {
    local name err
    
    name="$1"
    err="$2"
    echo "Usage:"
    echo "  $name"
    echo 
    echo "  Run the command from your normal user account"
    exit $err
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
    elif [ "$rel" != "10.10" ]; then
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

    mkreqdir "$GEM_TMPDIR"
    rm -rf "$GEM_TMPDIR"/*

    mkreqdir "$GEM_BASEDIR"

    distdesc=" $(lsb_release  -d | sed 's/Description:[ 	]*//g')" 
    if [ $ret -eq 1 ]; then
        echo "WARNING: this script is designed to run on Ubuntu 10.10, not on ${distdesc}." 
        read -p "press ENTER to continue AT YOUR OWN RISK or CTRL+C to abort." a
    elif [ $ret -eq 2 ]; then
        echo "ERROR: ${distdesc} not supported" 
        exit 1
    fi
    
    ###
    echo "== General requirements ==" 
    apt-get install -y git ant openjdk-6-jdk

    ###
    echo "== Geonode installation==" 
    defa="$GEM_HOSTNAME"
    read -p "Public site url or public IP address [$defa]: " SITE_URL
    if [ "$SITE_URL" = "" ]; then
        SITE_URL="$defa"
    fi
    export SITE_URL
    apt-get install -y python-software-properties
    add-apt-repository ppa:geonode/release
    if [ -f /etc/apt/sources.list.d/geonode-release-maverick.list ]; then
        mv /etc/apt/sources.list.d/geonode-release-maverick.list /etc/apt/sources.list.d/geonode-release-natty.list
        sed -i 's/maverick/natty/g' /etc/apt/sources.list.d/geonode-release-natty.list
    else
        echo "add-apt-repository ppa:geonode/release command failed"
        echo "installation ABORTED"
        exit 1
    fi  
    apt-get update
    export PATH=/usr/lib/python-django/bin:$PATH
    export VIRTUALENV_SYSTEM_SITE_PACKAGES=true
    apt-get install -y geonode
    
    sed -i "s@^ *SITEURL *=.*@SITEURL = 'http://$SITE_URL/'@g" "$GEM_GN_LOCSET"
    grep -q '^WSGIDaemonProcess.*:/var/lib/geonode/src/GeoNodePy/geonode' /etc/apache2/sites-available/geonode 
    if [ $? -ne 0 ]; then
        sed -i 's@\(^WSGIDaemonProcess.*$\)@\1:/var/lib/geonode/src/GeoNodePy/geonode@g' /etc/apache2/sites-available/geonode
    fi

    service tomcat6 restart
    service apache2 restart
    wget --save-headers -O "$GEM_TMPDIR/test_geonode.html" "http://$SITE_URL/"

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
        
    sudo -u $norm_user -i "cd $norm_dir ; git clone git://github.com/tuttle/django-schemata.git"
    mkreqdir -d "$GEM_BASEDIR"/django-schemata
    cd django-schemata
    git archive $GEM_DJANGO_SCHEMATA_GIT_VERS | tar -x -C "$GEM_BASEDIR"/django-schemata
    ln -s "$GEM_BASEDIR"/django-schemata/django_schemata /var/lib/geonode/src/GeoNodePy/geonode
    cd -
    apt-get install -y python-django-south

    ###
    #  Django-South configuration

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
  '$SITE_URL': {
    'schema_name': 'public',
    }
  }" >> "$GEM_GN_LOCSET"
    else
        schemata_config_add "$SITE_URL" "public"
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

    sudo -u postgres -i "\
dropdb $GEM_DB_NAME || true ; \
createdb -O $GEM_DB_USER $GEM_DB_NAME ; \
createlang plpgsql $GEM_DB_NAME ; \
psql -f $GEM_POSTGIS_PATH/postgis.sql $GEM_DB_NAME ; \
psql -f $GEM_POSTGIS_PATH/spatial_ref_sys.sql $GEM_DB_NAME ; \
"
    
    sed -i "s/DATABASE_NAME[ 	]*=[ 	]*'\([^']*\)'/DATABASE_NAME = '$GEM_DB_NAME'/g" "$GEM_GN_LOCSET"
    
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
        sed -i "s/^\(ORIGINAL_BACKEND[ 	]*=[ 	]*['\"]\)[0-9\.]\+\(.*\)/\1django.contrib.gis.db.backends.postgis\2/g" "$GEM_GN_LOCSET"
    else
        echo "ORIGINAL_BACKEND = 'django.contrib.gis.db.backends.postgis'" >> "$GEM_GN_LOCSET"
    fi

    ###
    echo "== Add 'geodetic' and 'observations' Django applications =="

    sudo -u $norm_user -i "cd $norm_dir ; git clone git://github.com/gem/oq-ui-api.git"
    mkreqdir -d "$GEM_BASEDIR"/oq-ui-api
    cd oq-ui-api
    git archive $GEM_OQ_UI_API_GIT_VERS | tar -x -C "$GEM_BASEDIR"/oq-ui-api
    ln -s "$GEM_BASEDIR"/oq-ui-api/geonode/geodetic     /var/lib/geonode/src/GeoNodePy/geonode/geodetic
    ln -s "$GEM_BASEDIR"/oq-ui-api/geonode/observations /var/lib/geonode/src/GeoNodePy/geonode/observations
     
    ##
    # /etc/geonode/local_settings.py    
    schemata_config_add 'geodetic' 'geodetic'
    schemata_config_add 'observations' 'gem'

    ##
    # /var/lib/geonode/src/GeoNodePy/geonode/settings.py    
    installed_apps_add 'geonode.observations'
    installed_apps_add 'geonode.geodetic'

    ##
    # deploy database
    cd /var/lib/geonode/
    source bin/activate
    cd src/GeoNodePy/geonode/
    python ./manage.py manage_schemata
    export DJANGO_SCHEMATA_DOMAIN="$SITE_URL"
    python ./manage.py syncdb
    export DJANGO_SCHEMATA_DOMAIN=geodetic
    python ./manage.py migrate geodetic
    export DJANGO_SCHEMATA_DOMAIN=observations
    python ./manage.py migrate observations
    deactivate
    
    cd $norm_dir

    ##
    echo "Add 'FaultedEarth' and 'geodetic'' client applications"

    sudo su - nastasi -c "
cd \"$norm_dir\"
git clone git://github.com/gem/oq-ui-client.git
cd oq-ui-client
git checkout $GEM_OQ_UI_CLIENT_GIT_VERS
git submodule init
git submodule update
ant init
ant debug -Dapp.port=8081 &
debug_pid=\$!
sleep 10
kill -0 \$debug_pid
if [ \$? -ne 0 ]; then
    echo \"oq-ui-client checkpoint\"
    echo \"ERROR: 'ant debug' failed\"
    exit 4
fi
kill -TERM \$debug_pid
exit 0
"
    ret=$?
    if [ $ret -ne 0 ]; then
        exit $ret
    fi
    
    ## 
    # FaultedEarth 
    sudo su - nastasi -c "
cd \"$norm_dir\"
cd oq-ui-client
sed -i 's@\(<project name=\"\)[^\"]*\(\" \)@\1FaultedEarth\2@g;s/^\( *\).*\(Build File.*\)$/\1FaultedEarth \2/g' build.xml
cp app/static/index_FE_fault.html app/static/index.html 
ant static-war
"
    cp oq-ui-client/build/FaultedEarth.war /var/lib/tomcat6/webapps/

    ##
    # geodetic
    sudo su - nastasi -c "
cd \"$norm_dir\"
cd oq-ui-client
sed -i 's@\(<project name=\"\)[^\"]*\(\" \)@\1geodetic\2@g;s/^\( *\).*\(Build File.*\)$/\1geodetic \2/g' build.xml
cp app/static/index_geodetic.html app/static/index.html 
ant static-war
"
    cp oq-ui-client/build/geodetic.war /var/lib/tomcat6/webapps/
 
    ##
    # configuration
    apache_append_proxy 'ProxyPass /FaultedEarth http://localhost:8080/FaultedEarth'
    apache_append_proxy 'ProxyPassReverse /FaultedEarth http://localhost:8080/FaultedEarth'
    apache_append_proxy 'ProxyPass /geodetic http://localhost:8080/geodetic'
    apache_append_proxy 'ProxyPassReverse /geodetic http://localhost:8080/geodetic'

    service tomcat6 restart
    service apache2 restart

    ###
    # custom geoserver installation

    service tomcat6 stop
    
    sudo -u $norm_user -i "cd $norm_dir ; git clone git://github.com/gem/oq-ui-geoserver.git"
    mkreqdir -d "$GEM_BASEDIR"/oq-ui-geoserver
    cd oq-ui-geoserver
    git archive $GEM_OQ_UI_GEOSERVER_GIT_VERS | tar -x -C "$GEM_BASEDIR"/oq-ui-geoserver
    chown -R tomcat6.tomcat6 "$GEM_BASEDIR"/oq-ui-geoserver
    if [ -d /var/lib/tomcat6/webapps/geoserver -a ! -L /var/lib/tomcat6/webapps/geoserver ]; then
        mv /var/lib/tomcat6/webapps/geoserver "$GEM_BASEDIR"/geoserver.orig
    fi

    ln -s "$GEM_BASEDIR"/oq-ui-geoserver/geoserver /var/lib/tomcat6/webapps/geoserver
    cd -

    ##
    # configuration
    cat /var/lib/tomcat6/webapps/geoserver/WEB-INF/web.xml | \
        sed -n '/^.*<param-name>GEONODE_BASE_URL<\/param-name>/{p;n;x;d};p'   | sed "s@^\( *\)\(<param-name>GEONODE_BASE_URL</param-name>.*\)@\1\2\n\1<param-value>http://$SITE_URL/</param-value>@g" | \
        sed -n '/^.*<param-name>GEOSERVER_DATA_DIR<\/param-name>/{p;n;x;d};p' | sed "s@^\( *\)\(<param-name>GEOSERVER_DATA_DIR</param-name>.*\)@\1\2\n\1<param-value>/var/lib/tomcat6/webapps/geoserver/data/</param-value>@g" > $GEM_TMPDIR/web.xml.new
    cp $GEM_TMPDIR/web.xml.new /var/lib/tomcat6/webapps/geoserver/WEB-INF/web.xml

    service tomcat6 start

#
#  THE END
#

    # echo "From root we have: norm_user: $norm_user  norm_dir: $norm_dir SITE_URL: $SITE_URL"
    return 0    
}

#
#  MAIN
#
wai="$(whoami)"

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

