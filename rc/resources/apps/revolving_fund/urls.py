from django.conf.urls.defaults import patterns, url
from django.views.generic.list import ListView
from rc.resources.apps.revolving_fund.models import RevolvingLoanFund


urlpatterns = patterns(
    '',

    url(r'^revolving-loan-funds', ListView.as_view(
            model=RevolvingLoanFund),
        name='revolving-loan-index'),
    
    )
