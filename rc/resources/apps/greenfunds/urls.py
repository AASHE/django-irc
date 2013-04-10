from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from models import GreenFund, StudentFeeFund, DonationFund, DepartmentFund, HybridFund
from rc.resources.apps.greenfunds.views import *
from haystack.forms import ModelSearchForm, SearchForm
from haystack.views import search_view_factory
from haystack.query import SearchQuerySet

sqs = SearchQuerySet().models(GreenFund)

# Create your views here.
urlpatterns = patterns('',
  # search
  url(r'^search/$',
  search_view_factory(
      view_class=FundSearchView,
      template='greenfunds/greenfund_search.html',
      searchqueryset=sqs,
      form_class=SearchForm),
      name='green-fund-search'),
  # CRUD URLs
  url(r'^add/success/$', TemplateView.as_view(
          template_name='greenfunds/crud_success.html'),
          name='green-fund-add-success'),
  url(r'^add/donation/$', login_required()(FundCreateView.as_view(model=DonationFund)),
      name="green-fund-add-donation"),
  url(r'^add/student-fee/$', login_required()(FundCreateView.as_view(model=StudentFeeFund)),
      name="green-fund-add-studentfee"),
  url(r'^add/department/$', login_required()(FundCreateView.as_view(model=DepartmentFund)),
      name="green-fund-add-department"),
  url(r'^add/hybrid/$', login_required()(FundCreateView.as_view(model=HybridFund)),
        name="green-fund-add-hybrid"),
  url(r'^add/$', TemplateView.as_view(
          template_name='greenfunds/greenfund_create_landing.html'),
          name='green-fund-add'),
  url(r'^edit/success/$', TemplateView.as_view(
          template_name='greenfunds/crud_success.html'),
      name='green-fund-edit-success'),    
  url(r'^edit/(?P<slug>[-\w]+)/$', login_required()(FundUpdateView.as_view()),
      name="green-fund-edit"),
  url(r'^edit/success/$', 'django.views.generic.base.TemplateView',
      {'template_name': 'greenfunds/crud_success.html'},
      name='green-fund-edit-success'),
  # End CRUD URLs
  # All funds
  url(r'^all/$', FundList.as_view(queryset=GreenFund.objects.filter(published=True)), 
    name='green-fund-list'),
  # Funds by State
  url(r'^state/(?P<state>[A-Z]+)/$', FundByState.as_view(), name='green-fund-state'),
  # Funds by Region
  url(r'^region/(?P<region>[\w-]+)/$', FundByRegion.as_view(), name='green-fund-region'),
  # Year
  url(r'^year/$', FundByYear.as_view(model=GreenFund,
    template_name='greenfunds/GreenFund_year_index.html'),
    name='green-fund-year-index'),
  url(r'^year/(?P<year>\d{4})/$', FundByYear.as_view(model=GreenFund), 
    name='green-fund-year'),
  # Map
  url(r'^map/$', FundMap.as_view(template_name='greenfunds/GreenFund_map.html'),
    name="green-fund-map"),
  # Control
  # url(r'^control/(?P<control>public|private)/$', FundTypeView.as_view(), 
  #   name='green-fund-control'),
  # Carnegie
  url(r'^carnegie/(?P<carnegie>.+)/$', FundCarnegieView.as_view(), name='green-fund-carnegie'), 
  # Members
  url(r'^member/$', FundByMember.as_view(), name='green-fund-member'), 
  # Homepage
  url(r'^$', FundIndex.as_view(
        queryset=GreenFund.objects.filter(published=True),
        template_name = 'greenfunds/index.html'),
        name="green-fund-index"),
  # Detail
  url(r'^(?P<slug>[-\w]+)/$', FundDetail.as_view(
    template_name = 'greenfunds/detail.html'), 
    name="green-fund-detail"),
  )