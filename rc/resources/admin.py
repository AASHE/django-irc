from django.contrib import admin


class ResourceItemAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'title', 'url', 'organization', 'notes', 'published')
    list_filter = ('published',)
    list_editable = ['title', 'url', 'organization', 'notes']
    
