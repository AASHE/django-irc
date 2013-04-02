from django.contrib import admin
from models import GreenFund, StudentFeeFund, DonationFund, DepartmentFund  

class GreenFundAdmin(admin.ModelAdmin):
    list_display = ('fund_name', 'institution', 'year')
    list_filter = ('published', 'year')

admin.site.register(StudentFeeFund, GreenFundAdmin)
admin.site.register(DonationFund, GreenFundAdmin)
admin.site.register(DepartmentFund, GreenFundAdmin)

