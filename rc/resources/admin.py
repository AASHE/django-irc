from django.contrib import admin
from aashe.organization.models import Organization


class ResourceItemAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'organization', 'notes', 'url', 'published')
    list_filter = ('published',)
    list_editable = ['published']
    search_fields = ['title', 'organization__name', 'description', 'notes']
    
    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == 'organization':
    #         kwargs['queryset'] = Organization.objects.filter(sector='Campus')
    #     return super(ResourceItemAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
    
