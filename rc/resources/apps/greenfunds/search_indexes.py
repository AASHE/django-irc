import datetime
from haystack.indexes import *
from haystack import site
from models import GreenFund, StudentFeeFund, DonationFund, DepartmentFund

# class StudentGreenFundIndex(SearchIndex):
#     text = CharField(document=True, use_template=True)
#     institution = CharField(model_attr='institution__name')
#     fund_name = CharField(model_attr='fund_name')
#     state = CharField(model_attr='institution__state')
#     city = CharField(model_attr='institution__city')

#     def index_queryset(self):
#         return StudentGreenFund.objects.filter(published=True)

# site.register(StudentGreenFund, StudentGreenFundIndex)