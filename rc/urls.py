from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

# monkey patch for longer menu captions
# TODO: use cursor to alter table at this point
from treemenus.models import MenuItem
MenuItem._meta.get_field('caption').max_length = 150 
if settings.DEBUG: cursor.execute("ALTER TABLE treemenus_menuitem MODIFY caption varchar(150)")

# auto discover admin classes
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^', include('rc.cms.urls')),
    (r'^', include('rc.resources.urls'))    
)
