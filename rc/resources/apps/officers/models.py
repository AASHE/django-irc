from gettext import gettext as _
from django.db import models
from aashe.organization.models import Organization

# Create your models here.
class CampusSustainabilityOfficer(models.Model):
    full_name = models.CharField(_('officer full name'), max_length=155, blank=True)
    title = models.CharField(_('officer title'), max_length=150, blank=True)
    email = models.EmailField(('officer email'), max_length=255)
    phone = models.CharField(_('officer phone number'), max_length=75, blank=True)
    web_page = models.CharField(('sustainability office web page'), max_length=75, blank=True)
    organization = models.ForeignKey(Organization, blank=True, null=True)

    class Meta:
        verbose_name = 'campus sustainability officer'
        verbose_name_plural = 'campus sustainability officers'

    class Admin:
        list_display = ('full_name', 'title',
                        'email', 'phone')
                        
    def __unicode__(self):
        return (self.full_name)