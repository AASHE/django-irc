from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from haystack.forms import ModelSearchForm, SearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView, search_view_factory
from rc.resources.apps.revolving_fund.models import RevolvingLoanFund
from rc.resources.apps.revolving_fund import views


sqs = SearchQuerySet().models(RevolvingLoanFund)

urlpatterns = patterns(
    '',

    url(r'^$',
        views.FundHomepage.as_view(
            queryset=RevolvingLoanFund.objects.published()),
        name='revolving-fund-index'),
    url(r'^all/$',
        views.FundListView.as_view(
            queryset=RevolvingLoanFund.objects.published()),
        name='revolving-fund-all'),
    url(r'^search/$',
        search_view_factory(
            view_class=views.FundSearchView,
            template='revolving_fund/revolvingloanfund_search.html',
            searchqueryset=sqs,
            form_class=SearchForm),
        name='revolving-fund-search'),
    url(r'^create/$',
        login_required(views.FundCreateView.as_view(),
                       login_url=reverse_lazy('accounts-login')),
        name='revolving-fund-create'),
    url(r'^create/success/$',
        views.FundListView.as_view(
            template_name='revolving_fund/revolvingloanfund_success.html',
            queryset=RevolvingLoanFund.objects.published()),
        name='revolving-fund-create-success'),
    url(r'^(?P<slug>[-\w]+)/update/$',
        login_required(views.FundUpdateView.as_view(
                model=RevolvingLoanFund), login_url=reverse_lazy('accounts-login')),
        name='revolving-fund-update'),
    url(r'^update/success/$',
        views.FundListView.as_view(
            queryset=RevolvingLoanFund.objects.published(),
            template_name='revolving_fund/revolvingloanfund_success.html'),
        name='revolving-fund-update-success'),
    url(r'^top10/$',
        views.FundTop10.as_view(
            queryset=RevolvingLoanFund.objects.published()),
        name='revolving-fund-top10'),
    url(r'^year/$',
        views.FundByYear.as_view(
            model=RevolvingLoanFund,
            template_name='revolving_fund/revolvingloanfund_year_index.html'),
        name='revolving-fund-year-index'),
    url(r'^year/(?P<year>\d{4})/$',
        views.FundByYear.as_view(model=RevolvingLoanFund),
        name='revolving-fund-year'),
    url(r'^control/(?P<control>public|private)/$',
        views.FundTypeView.as_view(),
        name='revolving-fund-control'),
    url(r'^carnegie/(?P<carnegie>.+)/$',
        views.FundCarnegieView.as_view(),
        name='revolving-fund-carnegie'),    
    url(r'^1-million/$',
        views.FundListView.as_view(
            template_name='revolving_fund/revolvingloanfund_million.html',
            queryset=RevolvingLoanFund.objects.published().filter(
                total_funds__gte=1000000).order_by("-total_funds")),
        name='revolving-fund-million'),
    url(r'^region/(?P<region>[\w-]+)/$',
        views.FundByRegion.as_view(),
        name='revolving-fund-region'),
    url(r'^billion-dollar-green-challenge/$',
        views.FundListView.as_view(
            queryset=RevolvingLoanFund.objects.published().filter(
                billion_dollar=True),
            template_name='revolving_fund/revolvingloanfund_billion.html'),
        name='revolving-fund-billion'),    
    url(r'^state/(?P<state>[A-Z]+)/$',
        views.FundByState.as_view(),
        name='revolving-fund-state'),
    url(r'^member/$',
        views.FundByMember.as_view(),
        name='revolving-fund-member'),    
    url(r'^(?P<slug>[-\w]+)/$',
        views.FundDetailView.as_view(
            queryset=RevolvingLoanFund.objects.published()),
        name='revolving-fund-detail'),
    )
