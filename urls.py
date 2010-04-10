from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
import dselector


parser = dselector.Parser()
url = parser.url

admin.autodiscover()

urlpatterns = parser.patterns('',
    (r'', include('yadba.urls')),
    (r'admin/doc/!', include('django.contrib.admindocs.urls')),
    (r'admin/(.*)!', admin.site.root),
)

if settings.DEBUG:
    urlpatterns += parser.patterns('',
        (r'media/{path:any}', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
