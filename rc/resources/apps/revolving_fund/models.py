'''
The revolving loan fund app manages the revolving loan fund database.
'''
from datetime import date
from django.db import models
from aashe.organization.models import Organization
from aashe.utils.slugify import unique_slugify


class RevolvingLoanFundManager(models.Manager):
    def published(self):
        return self.filter(published=True)
    
class RevolvingLoanFund(models.Model):
    institution = models.ForeignKey(Organization)
    billion_dollar = models.BooleanField(
        verbose_name='Billion Dollar Green Challenge Participant?')
    fund_name = models.CharField(max_length=120,
                                 verbose_name='Name of Fund')
    slug = models.SlugField(blank=True, editable=False)
    description = models.TextField(blank=True)
    year = models.IntegerField(max_length=4, verbose_name='Year Established')
    total_funds = models.PositiveIntegerField(verbose_name='Total Committed Funds')
    total_funds_date = models.DateField(blank=True, null=True)
    document_url = models.URLField(blank=True, max_length=250)
    published = models.BooleanField(default=False)
    pub_date = models.DateField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    objects = RevolvingLoanFundManager()
    
    def __unicode__(self):
        return self.institution.name

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, '%s' % self.fund_name)
        if not self.pub_date and self.published:
            self.pub_date = date.today()
        super(RevolvingLoanFund, self).save(*args, **kwargs)

    class Meta:
        ordering = ('institution', 'year')
