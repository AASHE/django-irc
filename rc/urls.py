from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from aashe import moderation
from aashe.aasheauth.forms import LoginForm


admin.autodiscover()

moderation.auto_discover()

urlpatterns = patterns(
    '',
    (r'^admin/linkcheck/', include('linkcheck.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^moderation/', include('aashe.moderation.urls')),
    url(r'^campus-sustainability-revolving-loan-funds/',
        include('rc.resources.apps.revolving_fund.urls')),
    url(r'^accounts/login/$', 'aashe.aasheauth.views.login',
        {'template_name': 'auth/login.html',
         'authentication_form': LoginForm},
        name='accounts-login'),
    url(r'^accounts/logout/$', 'aashe.aasheauth.views.logout_then_login',
        {'login_url': reverse_lazy('accounts-login')},
        name='accounts-logout'),
    url(r'^academic-programs/', include('rc.resources.apps.academic_programs.urls')),
    ('', include('rc.resources.apps.education.urls')),
    ('', include('rc.resources.apps.operations.urls')),
    ('', include('rc.resources.apps.pae.urls')),
    ('', include('rc.resources.apps.policies.urls')),
    ('', include('rc.resources.apps.programs.urls')),
    ('', include('rc.resources.apps.officers.urls')),
    ('', include('rc.cms.urls')),    
    ('', include('rc.cms.urls')),
)
