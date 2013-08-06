import datetime
from haystack.indexes import *
from haystack import site
from models import GreenFund

class GreenFundIndex(RealTimeSearchIndex):
    text = CharField(document=True, use_template=True)
    fund_name = CharField(model_attr='fund_name')
    fund_description = CharField(model_attr='fund_description')
    institution = CharField(model_attr='institution__name')
    state = CharField(model_attr='institution__state')
    city = CharField(model_attr='institution__city')

    def index_queryset(self):
        return GreenFund.objects.filter(published=True)

site.register(GreenFund, GreenFundIndex)