from django.contrib import admin
from rc.resources.apps.officers.models import *

class CampusSustainabilityOfficerAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'organization', 
                    'title',)
admin.site.register(CampusSustainabilityOfficer, CampusSustainabilityOfficerAdmin)