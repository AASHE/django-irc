from django.conf.urls.defaults import patterns, include, url
from rc.resources.apps.officers.models import *
from rc.resources.apps.officers.views import *

urlpatterns = patterns('',
    (r'^', include('rc.resources.apps.officers.urls')),
    (r'^', include('rc.resources.apps.education.urls')),
    (r'^', include('rc.resources.apps.operations.urls')),
    (r'^', include('rc.resources.apps.pae.urls')),
    (r'^', include('rc.resources.apps.policies.urls')),
    (r'^', include('rc.resources.apps.programs.urls')),
    )
