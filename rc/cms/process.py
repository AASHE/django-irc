import urllib, urllib2
from BeautifulSoup import BeautifulSoup, NavigableString, Tag
from treemenus.models import MenuItem, Menu
from rc.cms.models import Page


from django.conf import settings
username = settings.AASHE_ACCOUNT_USERNAME
password = settings.AASHE_ACCOUNT_PASSWORD

AASHEOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
urllib2.install_opener(AASHEOpener)

def _login():
    # TODO: Add 'if not AASHEOpener.is_logged_in'
    post_url = 'http://www.aashe.org/user/login'
    params = urllib.urlencode({'name': username,
                               'pass': password,
                               'form_id': 'user_login',
                               'form_build_id': 'form-b0528de66df7ca2ec1ff2a7a86868049'})
    f = AASHEOpener.open(post_url, params)
    data = f.read()
    f.close()

def generate_pages():
    # get all menu items for AASHE RC Menu
    menu = Menu.objects.get(name="AASHE Resource Center")
    items = MenuItem.objects.filter(menu=menu)

    # For each menu item, create a page if it doesn't exist
    for item in items:
        try:
            page = Page.objects.get(menuitem=item)
        # If page exists for this menu item, do nothing, otherwise create a new page
        except:
            # Create a new page if the item has a url
            # TODO: only generate pages with relative URLs
            if item.url:
                # TODO: Build URL Path
                _login()
                if item.url[0:4] != "http":
                    item.url = "http://www.aashe.org/" + item.url
                page = AASHEOpener.open(item.url)
                soup = BeautifulSoup(
                    page, convertEntities=BeautifulSoup.HTML_ENTITIES)
                # Get content from page
                # TODO: Convert this to markdown
                try:
                    title = soup.find('h1', {'class': 'page-title'}).text
                    content = soup.find('div', {'class': 'content clear-block'}).text
                except:
                    title = item.caption
                    content = ""
                newpage = Page(title=title, path=item.url, published=True, content=content, menuitem=item)
                except:
                    newpage = Page(title=item.caption, path=item.url, published=True, menuitem=item)
                newpage.save()
                
