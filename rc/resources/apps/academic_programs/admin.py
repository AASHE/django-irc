from django.contrib import admin
from django import forms
from rc.resources.apps.academic_programs.models import AcademicProgram, ProgramType
from aashe.organization.models import Organization
from aashe.moderation.admin import ModeratedObjectAdmin


class AcademicProgramForm(forms.ModelForm):
    
    class Meta:
        model = AcademicProgram

class AcademicProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ['title']
    admin_integration_enabled = True
    form = AcademicProgramForm
    fieldsets = (
    ('Basic Information', {'fields': ('title', 'program_type', 'institution',
                       'other_inst', 'description')}),
    ('Program Location', {
            'fields': ('location_name', 'city', 'state', 'country')}),
    ('Program Details', {
            'fields': ('department', 'duration', 'founded',
                       'distance_ed', 'commitment',
                       'language', 'discipline')}),
    ('Program Links', {
            'fields': ('blog',
                       'linkedin',
                       'facebook',
                       'twitter',
                       'homepage')}),
    ('Public Contact #1', {
            'classes': ('collapse',),
            'description': "Public contact information displayed as part of this program's detail page.",
            'fields': ('project_contact1_firstname', 'project_contact1_middle',
                       'project_contact1_lastname', 'project_contact1_title',
                       'project_contact1_phone', 'project_contact1_department',
                       )}),
    )

admin.site.register(AcademicProgram, AcademicProgramAdmin)

class ProgramTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']

admin.site.register(ProgramType, ProgramTypeAdmin)