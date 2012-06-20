# https://docs.djangoproject.com/en/1.4/howto/custom-template-tags/#code-layout
from django import template
from django.template.loader import render_to_string
from django.core.urlresolvers import resolve
from treemenus.models import MenuItem, Menu

register = template.Library()

def prepend_slash(value):
    if value.startswith('http'):
        return value
    else:
        return '/' + value

register.filter('prepend_slash', prepend_slash)

def generate_breadcrumb(object, request):
    if hasattr(object, 'menuitem'):
        menuitem = object.menuitem
        menu = menuitem.menu
        itemslist = []
        itemslist.append(menuitem)
        while menuitem != menu.root_item:
            menuitem = menuitem.parent
            itemslist.insert(0, menuitem)
        try:
            first, second, third = itemslist[1], itemslist[2], itemslist[-1]
            if second != third:
                itemslist = [first, second, third]
            else:
                itemslist = [first]
        except:
            first, second = itemslist[1], itemslist[-1]
            if first != second:
              itemslist = [first, second]
            else:
              itemslist = [first]
        # show the page title, not the menuitem title for the last item
        itemslist[-1].extension.caption = object.title
        return render_to_string('treemenus/breadcrumb_fragment.html', {'itemslist': itemslist})
    else:
        # this doesn't work anymore
        # view = resolve(request.path)
        # this removes the resources/ from the path
        new_path = request.path.split('/')
        resolve_path = new_path[2]
        resolve_path = "/%s" % resolve_path
        view = resolve(resolve_path)
        named_url = view.url_name
        try:
            menuitem = MenuItem.objects.filter(named_url=named_url)[0]
            menu = menuitem.menu
            itemslist = []
            itemslist.append(menuitem)
            while menuitem != menu.root_item:
                menuitem = menuitem.parent
                itemslist.insert(0, menuitem)
            first, second, third = itemslist[1], itemslist[2], itemslist[-1]
            if first != second:
              itemslist = [first, second, third]
            else:
              itemslist = [first]
            return render_to_string('treemenus/breadcrumb_fragment.html', {'itemslist': itemslist})
        except:
            pass

register.filter('generate_breadcrumb', generate_breadcrumb)

def generate_sidebar(object, request):
    # This code is for pages and other objects that have a MenuItem foreign key on the model
    if hasattr(object, 'menuitem'):
        # TODO: Implement this
        return render_to_string('treemenus/sidebar_fragment.html', {'itemslist': itemslist, 'childlist': childlist, 'activeitem': activeitem})
    # this is for views and other objects without MenuItem foreign keys
    else:
        # get view and named url
        # see comments in generate_breadcrumb
        new_path = request.path.split('/')
        resolve_path = new_path[2]
        resolve_path = "/%s" % resolve_path
        view = resolve(resolve_path)
        named_url = view.url_name
        try:
            menuitem = MenuItem.objects.filter(named_url=named_url)[0]
            menu = menuitem.menu
            # create lists
            # item list: all menu items
            # childlist: submenu items
            itemslist = []
            childlist = []
            # populate top-level menu
            for child in menu.root_item.children():
                itemslist.append(child)
            # populate submenu
            # no need to include stuff that's already in itemlist
            while menuitem.level > 1:
                # populate and sort the submenu children
                if menuitem.level == 2:
                    # activeitem is used to show active item in the sidebar
                    activeitem = menuitem
                    # get siblings of current menu item
                    for sibling in menuitem.siblings():
                       childlist.append(sibling)
                    childlist.append(activeitem)
                    # sort the list
                    childlist.sort(key=lambda x: x.rank)
                    # get the parent, though it isn't shown it is used for display purposes
                    menuitem = menuitem.parent
                    # don't change this, the parent has to be at the beginning of the list
                    childlist.insert(0, menuitem)
                # if we're deeper than level 2, go up but don't add the item to the list
                elif menuitem.level > 2:
                    menuitem = menuitem.parent
            return render_to_string('treemenus/sidebar_fragment.html', {'itemslist': itemslist, 'childlist': childlist, 'activeitem': activeitem})
        except:
            pass

register.filter('generate_sidebar', generate_sidebar)

def resource_menu(object):
  return render_to_string('treemenus/contentmenu_fragment.html', {'itemslist': itemslist, 'depth_to_render': depth_to_render})

register.filter('resource_menu', resource_menu)
