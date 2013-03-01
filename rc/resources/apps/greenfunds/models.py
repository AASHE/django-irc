from django.db import models
from aashe.organization.models import Organization
from aashe.utils.slugify import unique_slugify

# Commitment
COMMITMENT_CHOICES = (
	('MA', 'Mandatory')
    ('OI', 'Opt-in'),
    ('OO', 'Opt-out')
)
# Term length
TERM_CHOICES = (
    ('SM', 'Semester'),
    ('QA', 'Quarter'),
    ('CR', 'Credit'),
    ('AN', 'Anually'),
    ('TM', 'Trimester'),
    ('TR', 'Term')
)
# Currency
CURRENCY_CHOICES = (
    ('US', 'US Dollar'),
    ('CA', 'Canadian Dollar'),
    ('OT', 'Other')
)

# Create your models here.
class StudentGreenFund(models.Model):
	fund_name = models.CharField(_('fund name'), max_length=255)
	institution = institution = models.ForeignKey("organization.Organization", 
                                  help_text="Select the institution or organization that administers this fund",
                                  blank=True, null=True)
	year = models.IntegerField(max_length=4, verbose_name='Year Established')
	rate_per_term = models.DecimalField(decimal_places=2, verbose_name='Rate per term',
                             help_text='Enter the fund\s rate per term. No dollar signs', blank=True)
	rate_per_term_currency = models.CharField(choices=CURRENCY_CHOICES,
                                     max_length=5,
                                     help_text='Enter the currency of the fund\'s fee')
    mandatory = models.CharField(choices=COMMITMENT_CHOICES,
                                     max_length=5,
                                     help_text='Is this fund\'s fee mandatory, opt-in, or opt-out?')
    term = models.CharField(choices=TERM_CHOICES,
                                 max_length=5,
                                 help_text='Please select the term of this fund\'s fee.')
    homepage = models.URLField(max_length=255, 
                           help_text="Enter the URL for the program's website.")

    project_contact1_firstname = models.CharField(blank=True, max_length=75,
                                                  verbose_name='First name')
    project_contact1_middle = models.CharField(blank=True, max_length=75,
                                               verbose_name='Middle name/initial')
    project_contact1_lastname = models.CharField(blank=True, max_length=75,
                                                 verbose_name='Last name')
    project_contact1_email = models.EmailField(blank=True, verbose_name='Email')
    project_contact1_title = models.CharField(blank=True, max_length=75,
                                              verbose_name='Title/Position')
    project_contact1_phone = models.CharField(blank=True, max_length=75,
                                              verbose_name='Phone')
    project_contact1_department = models.CharField(blank=True, max_length=75,
                                                   verbose_name='Department')
    project_contact1_confirm = models.BooleanField(
        verbose_name='Confirm permission',
        help_text='Check this box to confirm you have obtained permission to provide this contact information.')
    published = models.BooleanField(_("is published"), blank=True)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    updated_date = models.DateTimeField(auto_now=True, editable=False)

    def project_contact1_details(self):
        if not self.project_contact1_firstname:
            return None
        name = u'%s %s' % (self.project_contact1_firstname, self.project_contact1_lastname)
        if self.project_contact1_title:
            name += u', %s' % self.project_contact1_title
        return name

    def save(self, *args, **kwargs):
        if not self.slug:
          unique_slugify(self, '%s' % (self.fee_name))
          
        super(StudentGreenFund, self).save()

    def __unicode__(self):
        return self.fee_name