from django.contrib import admin


class ResourceItemAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'url', 'organization', 'published')
    list_filter = ('published',)
    list_editable = ['url']
    
