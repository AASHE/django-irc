from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from rc.resources.apps.greenfunds.models import StudentGreenFund
from rc.resources.apps.greenfunds.views import *
from haystack.views import search_view_factory
from haystack.query import SearchQuerySet

# Create your views here.
urlpatterns = patterns('',
  # CRUD URLs
  url(r'^add/success/$', TemplateView.as_view(
          template_name='greenfunds/crud_success.html'),
      name='fund-add-success'),
  url(r'^add/$', login_required()(FundCreateView.as_view()),
      name="fund-add"),
  url(r'^edit/success/$', TemplateView.as_view(
          template_name='greenfunds/crud_success.html'),
      name='fund-edit-success'),    
  url(r'^edit/(?P<slug>[-\w]+)/$', login_required()(FundUpdateView.as_view()),
      name="fund-edit"),
  url(r'^edit/success/$', 'django.views.generic.base.TemplateView',
      {'template_name': 'greenfunds/crud_success.html'},
      name='fund-edit-success'),
  url(r'^$', FundList.as_view(
        template_name = 'greenfunds/index.html',
        queryset=StudentGreenFund.objects.all()), name="fund-index-view"),     
  url(r'^(?P<slug>[-\w]+)/$', FundDetail.as_view(template_name = 'greenfunds/detail.html'), 
   name="fund-detail-view"),
        )