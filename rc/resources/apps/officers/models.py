from gettext import gettext as _
from django.db import models
from aashe.organization.models import Organization

# Create your models here.
class CampusSustainabilityOfficer(models.Model):
    prefix = models.CharField(_('officer name prefix'), max_length=75, blank=True)
    first_name = models.CharField(_('officer first name'), max_length=75)
    middle_name = models.CharField(_('officer middle name or initial'), max_length=75, blank=True)
    last_name = models.CharField(_('officer last name'), max_length=75)
    title = models.CharField(_('officer title'), max_length=150, blank=True)
    email = models.EmailField(('officer email'), max_length=255)
    phone = models.CharField(_('officer phone number'), max_length=75, blank=True)
    web_page = models.CharField(('sustainability office web page'), max_length=75, blank=True)
    organization = models.ForeignKey(Organization, blank=True, null=True)

    class Meta:
        ordering = ('last_name', 'first_name')
        verbose_name = 'campus sustainability officer'
        verbose_name_plural = 'campus sustainability officers'

    class Admin:
        list_display = ('last_name', 'first_name', 'title',
                        'email', 'phone')
                        
    def __unicode__(self):
        return (self.first_name + ' ' + self.last_name)