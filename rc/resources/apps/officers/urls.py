from django.conf.urls.defaults import patterns, url

from rc.resources.apps.officers import models, views

urlpatterns = patterns('',
    url(r'^directory-campus-sustainability-officers$', OfficerList.as_view(
              template_name='officers/directory.html'),
              name='officers-directory'),
    )