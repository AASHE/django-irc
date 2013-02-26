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
    institution = models.ForeignKey(Organization, verbose_name='Institution')
    billion_dollar = models.BooleanField(
        verbose_name='Billion Dollar Green Challenge Participant?',
        help_text='Select this if the institution is participaing in the Billion Dollar Green Challenge.')
    fund_name = models.CharField(max_length=120,
                                 verbose_name='Name of Fund')
    slug = models.SlugField(blank=True, editable=False)
    description = models.TextField(blank=True)
    year = models.IntegerField(max_length=4, verbose_name='Year Established')
    total_funds = models.PositiveIntegerField(verbose_name='Total Committed Funds (USD)',
                                              help_text='Use whole numbers without commas.')
    total_funds_date = models.DateField(blank=True, null=True)
    document_url = models.URLField(blank=True, max_length=250, verbose_name='URL')
    published = models.BooleanField(default=False)
    pub_date = models.DateField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now=True)
    funded_projects = models.IntegerField(
        verbose_name='Number of Funded Projects (est.)',
        help_text='The count of projects this fund has supported.',
        blank=True, null=True)
    estimated_roi=models.IntegerField(
        verbose_name='Estimated Return on Investment',
        blank=True, null=True)
    contact_first_name = models.CharField(blank=True, max_length=75)
    contact_last_name = models.CharField(blank=True, max_length=75)
    contact_email = models.EmailField(blank=True)
    contact_title = models.CharField(blank=True, max_length=120)
    objects = RevolvingLoanFundManager()
    
    def __unicode__(self):
        return self.institution.name

    def contact_name_and_title(self):
        if self.contact_first_name and self.contact_last_name:
            name = u'%s %s' % (self.contact_first_name, self.contact_last_name)
            if self.contact_title:
                name += u' (%s)' % self.contact_title
            return name
        else:
            return u''

    @models.permalink
    def get_absolute_url(self):
        return ('revolving-fund-detail', (), {'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, '%s' % self.fund_name)
        if not self.pub_date and self.published:
            self.pub_date = date.today()
        super(RevolvingLoanFund, self).save(*args, **kwargs)

    class Meta:
        ordering = ('institution', 'year')
