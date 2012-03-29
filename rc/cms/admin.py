from django.contrib import admin
from rc.cms.models import Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'menuitem')
    list_filter = ('published',)
admin.site.register(Page, PageAdmin)
