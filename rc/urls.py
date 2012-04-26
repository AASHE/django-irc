from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

# auto discover admin classes
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^', include('rc.cms.urls')),
    (r'^', include('rc.resources.urls'))    
)
