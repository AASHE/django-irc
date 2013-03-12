from django.contrib import admin
from models import StudentGreenFund

class StudentGreenFundAdmin(admin.ModelAdmin):
    list_display = ('fund_name', 'institution', 'year')
    list_filter = ('published', 'year')

admin.site.register(StudentGreenFund, StudentGreenFundAdmin)
