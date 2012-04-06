from BeautifulSoup import BeautifulSoup, NavigableString, Tag
from treemenus.models import MenuItem, Menu
from rc.cms.models import Page
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    # Process all menu items
    def generate_pages():
        # get all menu items for AASHE RC Menu
        menu = Menu.objects.get(name="AASHE Resource Center")
        items = MenuItem.objects.filter(menu=menu)
    
        # For each menu item, create a page if it doesn't exist
        for item in items:
            page = page.objects.get(menuitem=item)
            # If page exists for this menu item, do nothing, otherwise create a new page
            if page:
                pass
            else:
                # Create a new page
                # TODO: Build URL Path
                # TODO: Get markdown content from page
                page = Page(title=item.caption, path=item.url, published=True, menuitem=item)
                page.Save()