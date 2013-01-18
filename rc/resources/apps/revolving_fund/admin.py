from django.contrib import admin
from rc.resources.apps.revolving_fund.models import RevolvingLoanFund



class RevolvingLoanFundAdmin(admin.ModelAdmin):
    list_display = ('fund_name', 'institution', 'year', 'total_funds')
admin.site.register(RevolvingLoanFund, RevolvingLoanFundAdmin)
