from django.conf.urls.defaults import patterns, url
from haystack.forms import ModelSearchForm, SearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView, search_view_factory
from rc.resources.apps.revolving_fund.models import RevolvingLoanFund
from rc.resources.apps.revolving_fund import views


sqs = SearchQuerySet().models(RevolvingLoanFund)

urlpatterns = patterns(
    '',

    url(r'^revolving-loan-funds/$', views.FundHomepage.as_view(
            queryset=RevolvingLoanFund.objects.published()),
        name='revolving-fund-index'),
    url(r'^revolving-loan-funds/all/$', views.FundListView.as_view(
            queryset=RevolvingLoanFund.objects.published()),
        name='revolving-fund-all'),
    url(r'^revolving-loan-funds/search/$', search_view_factory(
            view_class=views.FundSearchView,
            template='revolving_fund/revolvingloanfund_search.html',
            searchqueryset=sqs,
            form_class=SearchForm),
        name='revolving-fund-search'),
    url(r'^revolving-loan-funds/create/$', views.FundCreateView.as_view(),
        name='revolving-fund-create'),
    url(r'^revolving-loan-funds/(?P<slug>[-\w]+)/update/$',
        views.FundUpdateView.as_view(
            model=RevolvingLoanFund),
        name='revolving-fund-update'),
    url(r'^revolving-loan-funds/top10/$',
        views.FundTop10.as_view(
            queryset=RevolvingLoanFund.objects.published()),
        name='revolving-fund-top10'),
    url(r'^revolving-loan-funds/year/(?P<year>\d{4})/$',
        views.FundByYear.as_view(model=RevolvingLoanFund),
        name='revolving-fund-year'),
    url(r'^revolving-loan-funds/control/(?P<control>public|private)/$',
        views.FundTypeView.as_view(),
        name='revolving-fund-control'),
    url(r'^revolving-loan-funds/carnegie/(?P<carnegie>.+)/$',
        views.FundCarnegieView.as_view(),
        name='revolving-fund-carnegie'),    
    url(r'^revolving-loan-funds/1-million/$',
        views.FundListView.as_view(
            template_name='revolving_fund/revolvingloanfund_million.html',
            queryset=RevolvingLoanFund.objects.published().filter(
                total_funds__gte=1000000).order_by("-total_funds")),
        name='revolving-fund-million'),
    url(r'^revolving-loan-funds/region/(?P<region>[\w-]+)/$',
        views.FundByRegion.as_view(),
        name='revolving-fund-region'),
    url(r'^revolving-loan-funds/billion-dollar-green-challenge/$',
        views.FundListView.as_view(
            queryset=RevolvingLoanFund.objects.published().filter(
                billion_dollar=True),
            template_name='revolving_fund/revolvingloanfund_billion.html'),
        name='revolving-fund-billion'),    
    url(r'^revolving-loan-funds/state/(?P<state>[A-Z]+)/$',
        views.FundByState.as_view(),
        name='revolving-fund-state'),
    url(r'^revolving-loan-funds/member/$',
        views.FundByMember.as_view(),
        name='revolving-fund-member'),    
    url(r'^revolving-loan-funds/(?P<slug>[-\w]+)/$', views.FundDetailView.as_view(
            model=RevolvingLoanFund),
        name='revolving-fund-detail'),
    )
