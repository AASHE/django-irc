from django.contrib import admin
from django.contrib.contenttypes import generic
from models import GreenFund, StudentFeeFund, DonationFund, DepartmentFund, HybridFund 

class GreenFundInline(generic.GenericTabularInline):
    model = GreenFund

class GreenFundAdmin(admin.ModelAdmin):
    # list_display = ('fund_name', 'institution', 'year')
    # list_filter = ('published', 'year')
    inlines = [
    	GreenFundInline
    ]

admin.site.register(StudentFeeFund, GreenFundAdmin)
admin.site.register(DonationFund, GreenFundAdmin)
admin.site.register(DepartmentFund, GreenFundAdmin)
admin.site.register(HybridFund, GreenFundAdmin)
