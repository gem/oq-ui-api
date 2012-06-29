#!/bin/bash
export GEM_CERT_KEY=private_data/oq-platform.key
export GEM_CERT_CRT=private_data/oq-platform.crt
export GEM_APACHE_CONF=/etc/apache2/sites-available/geonode
export TB='	'
export NL='
'

#
#  MAIN
export norm_dir="$(pwd)/"
for reqfile in "${norm_dir}$GEM_CERT_KEY" "${norm_dir}$GEM_CERT_CRT" "$GEM_APACHE_CONF" ; do
    if [ ! -f "$reqfile" ]; then
        echo "$reqfile not found"
        exit 1
    fi
done

# enable ssl module
