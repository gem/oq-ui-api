#!/bin/bash
set -x

#
# PUBLIC GLOBAL VARS
# version managements - use "master" or tagname to move to other versions
export GEM_DJANGO_SCHEMATA_VERS=8f9487b70c9b1508ae70b502b950066147956993
export       GEM_OQ_UI_API_VERS=fc689867330f78c883d1283a2542bdba12835083
export    GEM_OQ_UI_CLIENT_VERS=2224d2eff6ca5ec8de33372a40a1c7fccaa0469f
export GEM_OQ_UI_GEOSERVER_VERS=fbe1f48f1e40dd91e1e2dfcad5bebaf20a208b1e
export GEM_DB_NAME="geonode_dev"

#
# PRIVATE GLOBAL VARS
export GEM_DB_USER="geonode"
export GEM_POSTGIS_PATH=/usr/share/postgresql/8.4/contrib/postgis-1.5
export GEM_HOSTNAME="$(hostname)"
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

geonode_installation () { 
    local norm_user norm_dir ret a distdesc
    local cur_step

    cur_step=0

    norm_user="$1"
    norm_dir="$2"

    #
    # Verify if the distribution is compliant with the script.
    check_distro
    ret=$?

    if [ ! -d gem_tmp ]; then
        mkdir gem_tmp
    fi

    if [ ! -d gem_tmp ]; then
        echo "ERROR: gem_tmp dir creation failed" 
        exit 1
    else
        rm -rf gem_tmp/*
    fi  

    distdesc=" $(lsb_release  -d | sed 's/Description:[ 	]*//g')" 
    if [ $ret -eq 1 ]; then
        echo "WARNING: this script is designed to run on Ubuntu 10.10, not on ${distdesc}." 
        read -p "press ENTER to continue AT YOUR OWN RISK or CTRL+C to abort." a
    elif [ $ret -eq 2 ]; then
        echo "ERROR: ${distdesc} not supported" 
        exit 1
    fi
    
if [ 0 -eq 1 ]; then
    # 
    echo "== General requirements ==" 
    apt-get install -y git ant openjdk-6-jdk

    #
    echo "== Geonode installation==" 
    apt-get install -y python-software-properties
    add-apt-repository ppa:geonode/release
    apt-get update
    export PATH=/usr/lib/python-django/bin:$PATH
    export VIRTUALENV_SYSTEM_SITE_PACKAGES=true
    apt-get install -y geonode
fi    
    
    read -p "Public site url or public IP address (es. 'http://www.example.com/' or 'http://$GEM_HOSTNAME/'): " SITE_URL
    sed -i "s@^ *SITEURL *=.*@SITEURL = '$SITE_URL'@g" /etc/geonode/local_settings.py
    grep -q '^WSGIDaemonProcess.*:/var/lib/geonode/src/GeoNodePy/geonode' /etc/apache2/sites-available/geonode 
    if [ $? -ne 0 ]; then
        sed -i 's@\(^WSGIDaemonProcess.*$\)@\1:/var/lib/geonode/src/GeoNodePy/geonode@g' /etc/apache2/sites-available/geonode
    fi

    service tomcat6 restart
    service apache2 restart
    wget --save-headers -O gem_tmp/test_geonode.html "$SITE_URL"

    head -n 1 gem_tmp/test_geonode.html > gem_tmp/test_geonode.http 
    grep -q 200 gem_tmp/test_geonode.http 
    if [ $? -ne 0 ]; then
        echo 
        echo "WARNING: GEONODE WEB TEST FAILED!"
        cat test_geonode.http
        echo
        read -p "press ENTER to continue or CTRL+C to abort:" a
    fi

    # 
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
    
    sed -i "s/DATABASE_NAME[ 	]*=[ 	]*'\([^']*\)'/DATABASE_NAME = '$GEM_DB_NAME'/g" /etc/geonode/local_settings.py
    
    service apache2 start
    service tomcat6 start

    echo "From root we have: $norm_user from $norm_dir dir SITE_URL $SITE_URL"
    
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
else
    usage "$0" 1
fi

echo "The end $(whoami)" 
exit 123

# check for the SO version

