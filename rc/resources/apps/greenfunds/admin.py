from django.contrib import admin
from django.contrib.contenttypes import generic
from models import GreenFund, StudentFeeFund, DonationFund, DepartmentFund, HybridFund, FundRecipient


class GreenFundAdmin(admin.ModelAdmin):
    search_fields = ['fund_name']

admin.site.register(StudentFeeFund, GreenFundAdmin)
admin.site.register(DonationFund, GreenFundAdmin)
admin.site.register(DepartmentFund, GreenFundAdmin)
admin.site.register(HybridFund, GreenFundAdmin)
admin.site.register(FundRecipient, admin.ModelAdmin)