from django.contrib import admin
from rc.cms.models import Page, MenuItemExtension
from treemenus.admin import MenuAdmin, MenuItemAdmin
from treemenus.models import Menu

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'menuitem')
    list_filter = ('published',)
admin.site.register(Page, PageAdmin)

class MenuItemExtensionInline(admin.StackedInline):
    model = MenuItemExtension
    max_num = 1

class CustomMenuItemAdmin(MenuItemAdmin):
    inlines = [MenuItemExtensionInline,]

class CustomMenuAdmin(MenuAdmin):
    menu_item_admin_class = CustomMenuItemAdmin

admin.site.unregister(Menu) # Unregister the standard admin options
admin.site.register(Menu, CustomMenuAdmin) # Register the new, customized, admin options


