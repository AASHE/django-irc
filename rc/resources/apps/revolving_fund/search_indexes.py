import datetime
from haystack.indexes import *
from haystack import site
from rc.resources.apps.revolving_fund.models import RevolvingLoanFund


class RevolvingLoanFundIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    institution = CharField(model_attr='institution__name')
    description = CharField(model_attr='description')
    fund_name = CharField(model_attr='fund_name')
    state = CharField(model_attr='institution__state')
    city = CharField(model_attr='institution__city')

    def index_queryset(self):
        return RevolvingLoanFund.objects.filter(published=True)

site.register(RevolvingLoanFund, RevolvingLoanFundIndex)
