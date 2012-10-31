from django.conf.urls.defaults import patterns, url
from rc.resources.apps.officers.models import *

urlpatterns = patterns('',
    url(r'^directory-campus-sustainability-officers$', stufipt.as_view(template_name = 'officers/directory.html'), 
     name="officers-directory"),
    )