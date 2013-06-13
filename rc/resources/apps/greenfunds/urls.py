from itertools import chain
from django.conf.urls.defaults import patterns, include, url
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from models import GreenFund, StudentFeeFund, DonationFund, DepartmentFund, HybridFund
from views import *
from haystack.forms import ModelSearchForm, SearchForm
from haystack.views import search_view_factory
from haystack.query import SearchQuerySet

sqs = SearchQuerySet().models(StudentFeeFund, DonationFund, DepartmentFund, HybridFund)

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
    url(r'^add/donation/$', login_required()(FundCreateView.as_view(model=DonationFund,
      form_class=DonationFundCreateForm)),
    name="green-fund-add-donation"),
    url(r'^add/student-fee/$', login_required()(FundCreateView.as_view(model=StudentFeeFund,
      form_class=StudentFeeFundCreateForm)),
    name="green-fund-add-studentfee"),
    url(r'^add/department/$', login_required()(FundCreateView.as_view(model=DepartmentFund,
      form_class=DepartmentFundCreateForm)),
    name="green-fund-add-department"),
    url(r'^add/hybrid/$', login_required()(FundCreateView.as_view(model=HybridFund,
    form_class=HybridFundCreateForm)),
    name="green-fund-add-hybrid"),
    url(r'^add/$', TemplateView.as_view(
      template_name='greenfunds/greenfund_create_landing.html'),
    name='green-fund-add'),
    url(r'^edit/success/$', TemplateView.as_view(
      template_name='greenfunds/crud_success.html'),
    name='green-fund-edit-success'),
    url(r'^hybrid/(?P<slug>[-\w]+)/edit$', login_required()(HybridFundUpdateView.as_view()),
      name="hybrid-fund-edit"),
    url(r'^department/(?P<slug>[-\w]+)/edit$', login_required()(DepartmentFundUpdateView.as_view()),
      name="department-fund-edit"),
    url(r'^donation/(?P<slug>[-\w]+)/edit$', login_required()(DonationFundUpdateView.as_view()),
      name="donation-fund-edit"),
    url(r'^student-fee/(?P<slug>[-\w]+)/edit$', login_required()(StudentFeeFundUpdateView.as_view()),
      name="fee-fund-edit"),
    url(r'^edit/success/$', 'django.views.generic.base.TemplateView',
      {'template_name': 'greenfunds/crud_success.html'},
      name='green-fund-edit-success'),
    # End CRUD URLs
    # All funds
    url(r'^all/$', FundList.as_view(queryset=list(chain(StudentFeeFund.objects.filter(published=True),
      DonationFund.objects.filter(published=True),
      DepartmentFund.objects.filter(published=True),
      HybridFund.objects.filter(published=True))), template_name='greenfunds/GreenFund_list.html',),
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
        queryset=list(chain(StudentFeeFund.objects.filter(published=True),
          DonationFund.objects.filter(published=True),
          DepartmentFund.objects.filter(published=True),
          HybridFund.objects.filter(published=True),)),
        template_name = 'greenfunds/index.html'),
        name="green-fund-index"),
    # Detail
    url(r'^hybrid/(?P<slug>[-\w]+)/$', HybridFundDetail.as_view(
        template_name = 'greenfunds/detail.html'),
        name="hybrid-fund-detail"),
    url(r'^department/(?P<slug>[-\w]+)/$', DepartmentFundDetail.as_view(
        template_name = 'greenfunds/detail.html'),
        name="department-fund-detail"),
    url(r'^student-fee/(?P<slug>[-\w]+)/$', StudentFeeFundDetail.as_view(
        template_name = 'greenfunds/detail.html'),
        name="fee-fund-detail"),
    url(r'^donation/(?P<slug>[-\w]+)/$', DonationFundDetail.as_view(
        template_name = 'greenfunds/detail.html'),
        name="donation-fund-detail"),
    )