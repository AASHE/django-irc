from datetime import datetime
from gettext import gettext as _
from django.db import models
from aashe.organization.models import Organization


class ResourceItemManager(models.Manager):
    def published(self):
        return self.filter(published=True)

class ResourceItem(models.Model):
    '''
    Abstract base-class to support commonality between all resources
    in the the resource center.
    '''
    title = models.CharField(_('resource title'), max_length=128)
    url = models.URLField(_('resource url'), blank=True)
    organization = models.ForeignKey(Organization, blank=True, null=True)
    description = models.TextField(_('resource description'), blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)
    published = models.BooleanField(_('published'), default=True)
    pub_date = models.DateTimeField(editable=False)
    notes = models.TextField(_('internal notes'), blank=True)
    objects = ResourceItemManager()
    
    class Meta:
        abstract = True

    def save(self):
        if self.published and not self.pub_date:
            self.pub_date = datetime.now()
        elif not self.published:
            self.pub_date = None
        super(ResourceItem, self).save()

    def __unicode__(self):
        return self.title
