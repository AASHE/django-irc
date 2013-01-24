from django.conf.urls.defaults import patterns, url
from rc.resources.apps.revolving_fund.models import RevolvingLoanFund
import views


urlpatterns = patterns(
    '',

    url(r'^revolving-loan-funds/$', views.FundHomepage.as_view(
            queryset=RevolvingLoanFund.objects.published()),
        name='revolving-fund-index'),
    url(r'^revolving-loan-funds/all/$', views.FundListView.as_view(
            queryset=RevolvingLoanFund.objects.published()),
        name='revolving-fund-all'),
    url(r'^revolving-loan-funds/year/(?P<year>\d{4})/$',
        views.FundByYear.as_view(),
        name='revolving-fund-year'),
    url(r'^revolving-loan-funds/1-million/$',
        views.FundListView.as_view(
            template_name='revolving_fund/1-million.html',
            queryset=RevolvingLoanFund.objects.published().filter(
                total_funds__gte=1000000)),
        name='revolving-fund-million'),
    url(r'^revolving-loan-funds/region/(?P<region>[\w-]+)/$',
        views.FundByRegion.as_view(
            model=RevolvingLoanFund),
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
