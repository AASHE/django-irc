'''
The `cms` app represents views and models for editing resource center
pages and resources.
'''
from gettext import gettext as _
from django.utils.translation import ugettext_lazy
from datetime import datetime
from django.db import models
from treemenus.models import Menu


class PageManager(models.Manager):
    def published(self):
        return self.filter(published=True)
    
class Page(models.Model):
    '''
    The Page model represents a page in the resource center. It allows
    for staff to edit page content. Page objects can contain other
    pages as well as Resources, which can be assigned to one or more
    pages (see rc.resources.models.Resource).
    '''
    title = models.CharField(_('page title'), max_length=128)
    path = models.SlugField(_('URL path'), max_length=128)
    published = models.BooleanField(_("is published"), blank=True)
    pub_date = models.DateTimeField(_("publication date"), null=True, blank=True, editable=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)
    content = models.TextField(_("page content"), blank=True)
    menu = models.ForeignKey(Menu, null=True, blank=True, related_name='pages',
                             verbose_name=ugettext_lazy('menu'))
    objects = PageManager()

    def __unicode__(self):
        return self.title

    def save(self):
        if self.published and not self.pub_date:
            self.pub_date = datetime.now()
        elif not self.published:
            self.pub_date = None
        super(Page, self).save()
