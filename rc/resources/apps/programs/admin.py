from django.contrib import admin
from rc.resources.apps.programs.models import *


class ProgramAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'published', 'type')
    list_filter = ('type', 'published')
admin.site.register(Program, ProgramAdmin)    
    
class ProgramTypeAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'type')
    list_editable = ['type']
admin.site.register(ProgramType, ProgramTypeAdmin)
