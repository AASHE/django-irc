from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns(
    '',
    (r'^admin/linkcheck/', include('linkcheck.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    ('', include('rc.resources.apps.education.urls')),
    ('', include('rc.resources.apps.operations.urls')),
    ('', include('rc.resources.apps.pae.urls')),
    ('', include('rc.resources.apps.policies.urls')),
    ('', include('rc.resources.apps.programs.urls')),
    ('', include('rc.resources.apps.officers.urls')),
    ('', include('rc.resources.apps.revolving_fund.urls')),
    ('', include('rc.cms.urls')),    
)
