from django.contrib import admin
from rc.academic_programs.models import AcademicProgram
from aashe.organization.models import Organization


class AcademicProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ['title']

admin.site.register(AcademicProgram, AcademicProgramAdmin)