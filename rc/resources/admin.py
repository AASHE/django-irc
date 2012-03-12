from django.contrib import admin


class ResourceItemAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'published')
    list_filter = ('published',)
    
