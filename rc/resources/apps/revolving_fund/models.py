'''
The revolving loan fund app manages the revolving loan fund database.
'''
from django.db import models
from aashe.organization.models import Organization


class RevolvingLoanFund(models.Model):
    institution = models.ForeignKey(Organization)
    billion_dollar = models.BooleanField(
        verbose_name='Billion Dollar Green Challenge Participant?')
    fund_name = models.CharField(max_length=120,
                                 verbose_name='Name of Fund')
    description = models.TextField(blank=True)
    year = models.IntegerField(max_length=4, verbose_name='Year Established')
    total_funds = models.PositiveIntegerField(verbose_name='Total Committed Funds')
    document_url = models.URLField(blank=True)
    
    def __unicode__(self):
        return self.institution.name

    class Meta:
        ordering = ('institution', 'year')
