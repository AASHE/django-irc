from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # (r'^admin/linkcheck', include('linkcheck.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^', include('rc.cms.urls')),
    (r'^', include('rc.resources.apps.education.urls')),
    (r'^', include('rc.resources.apps.operations.urls')),
    (r'^', include('rc.resources.apps.pae.urls')),
    (r'^', include('rc.resources.apps.policies.urls')),
    (r'^', include('rc.resources.apps.programs.urls'))
)
