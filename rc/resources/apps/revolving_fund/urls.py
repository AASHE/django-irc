from django.conf.urls.defaults import patterns, url
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rc.resources.apps.revolving_fund.models import RevolvingLoanFund
from views import FundHomepage, FundByState, FundListView


urlpatterns = patterns(
    '',

    url(r'^revolving-loan-funds/$', FundHomepage.as_view(
            model=RevolvingLoanFund),
        name='revolving-fund-index'),
    url(r'^revolving-loan-funds/all/$', FundListView.as_view(
            model=RevolvingLoanFund),
        name='revolving-fund-all'),
    url(r'^revolving-loan-funds/billion-dollar-green-challenge/$',
        FundListView.as_view(
            queryset=RevolvingLoanFund.objects.filter(billion_dollar=True),
            template_name='revolving_fund/revolvingloanfund_billion.html'),
        name='revolving-fund-billion'),    
    url(r'^revolving-loan-funds/state/(?P<state>[A-Z]+)/$',
        FundByState.as_view(),
        name='revolving-fund-state'),
    url(r'^revolving-loan-funds/(?P<slug>[-\w]+)/$', DetailView.as_view(
            model=RevolvingLoanFund),
        name='revolving-fund-detail'),
    )
