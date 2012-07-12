#!/bin/bash
#
# Description: 
#
# this is a workaround to allow our old-fashion applications
# to work with the new django 1.4 that add a new security
# tool (csrf) to POST and PUT methods using hidden vars 
#

cat <<EOF | patch -p0
--- null	2012-07-12 13:11:32.964981634 +0200
+++ /var/lib/geonode/src/GeoNodePy/geonode/proxy/views.py	2012-07-12 13:09:49.888983849 +0200
@@ -3,8 +3,10 @@
 from urlparse import urlsplit
 import httplib2
 from django.conf import settings
+from django.views.decorators.csrf import csrf_exempt
 
 
+@csrf_exempt
 def proxy(request):
     if 'url' not in request.GET:
         return HttpResponse(
EOF

