from django.contrib import admin
from rc.resources.apps.revolving_fund.models import RevolvingLoanFund



class RevolvingLoanFundAdmin(admin.ModelAdmin):
    list_display = ('fund_name', 'institution', 'year', 'total_funds')
    list_filter = ('billion_dollar', 'published', 'year')
    actions = ['add_billion_dollar', 'remove_billion_dollar']

    def remove_billion_dollar(modeladmin, request, queryset):
        # Admin action function to remove selected funds for Billion Dollar Challenge
        queryset.update(billion_dollar=False)
    remove_billion_dollar.short_description = 'Remove from Billion Dollar Challenge'

    def add_billion_dollar(modeladmin, request, queryset):
        # Admin action function to remove selected funds for Billion Dollar Challenge
        queryset.update(billion_dollar=True)
    add_billion_dollar.short_description = 'Add to Billion Dollar Challenge'
admin.site.register(RevolvingLoanFund, RevolvingLoanFundAdmin)
