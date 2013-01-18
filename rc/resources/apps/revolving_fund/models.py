'''
The revolving loan fund app manages the revolving loan fund database.
'''
from django.db import models
from aashe.organization.models import Organization
from aashe.utils.slugify import unique_slugify


class RevolvingLoanFund(models.Model):
    institution = models.ForeignKey(Organization)
    billion_dollar = models.BooleanField(
        verbose_name='Billion Dollar Green Challenge Participant?')
    fund_name = models.CharField(max_length=120,
                                 required=True,
                                 verbose_name='Name of Fund')
    slug = models.SlugField(blank=True, editable=False)
    description = models.TextField(blank=True)
    year = models.IntegerField(max_length=4, verbose_name='Year Established')
    total_funds = models.PositiveIntegerField(verbose_name='Total Committed Funds')
    total_funds_date = models.DateField(blank=True, null=True)
    document_url = models.URLField(blank=True)
    
    def __unicode__(self):
        return self.institution.name

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, '%s' % self.fund_name)
        super(RevolvingLoanFund, self).save(*args, **kwargs)

    class Meta:
        ordering = ('institution', 'year')
