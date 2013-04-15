from django.contrib import admin
from django.contrib.contenttypes import generic
from models import GreenFund, StudentFeeFund, DonationFund, DepartmentFund, HybridFund, FundTerm, FundRecipient

class GreenFundInline(generic.GenericStackedInline):
    model = GreenFund
    extra = 1
    max_num = 1

class FundTermInline(admin.TabularInline):
    model = FundTerm
    extra = 1

class GreenFundAdmin(admin.ModelAdmin):
    # TODO figure this out for generic relations
    # list_display = ('fund_data__fund_name')
    # list_filter = ('published', 'year')
    inlines = [
    	GreenFundInline,
        FundTermInline
    ]

admin.site.register(StudentFeeFund, GreenFundAdmin)
admin.site.register(DonationFund, GreenFundAdmin)
admin.site.register(DepartmentFund, GreenFundAdmin)
admin.site.register(HybridFund, GreenFundAdmin)
admin.site.register(FundTerm, admin.ModelAdmin)
admin.site.register(FundRecipient, admin.ModelAdmin)