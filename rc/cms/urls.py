from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import TemplateView
from rc.cms.views import PageView

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='cms/index.html')),
    url(r'^(?P<slug>.+)/$', PageView.as_view()),
    )
