from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    (r'^', include('rc.resources.apps.education.urls')),
    (r'^', include('rc.resources.apps.operations.urls')),
    )
