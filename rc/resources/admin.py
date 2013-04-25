from django.contrib import admin
from aashe.organization.models import Organization


class ResourceItemAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'organization', 'notes', 'url', 'updated_date','published')
    list_filter = ('published',)
    list_editable = ['published']
    search_fields = ['title', 'organization__name', 'description', 'notes']
    
