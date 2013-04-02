from gettext import gettext as _
from django.db import models
from aashe.organization.models import Organization
from aashe.utils.slugify import unique_slugify

# Commitment
COMMITMENT_CHOICES = (
    ('MA', 'Mandatory'),
    ('OI', 'Opt-in'),
    ('OO', 'Opt-out')
)
# Term length
TERM_CHOICES = (
    ('SM', 'semester'),
    ('QA', 'quarter'),
    ('CR', 'credit'),
    ('AN', 'annually'),
    ('TM', 'trimester'),
    ('TR', 'term')
)
# Fund Type
TYPE_CHOICES = (
    ('ON', 'Ongoing'),
    ('OT', 'One-time gift')
)
# Funding Source
SOURCE_CHOICES = (
    ('AL', 'Alumni'),
    ('FD', 'Foundation'),
    ('CP', 'Corporate/Commercial')
)

# Create your models here.
class GreenFund(models.Model):
    fund_name = models.CharField(_('fund name'), max_length=255)
    institution = institution = models.ForeignKey("organization.Organization", 
                                  help_text="Select the institution or organization that administers this fund",
                                  blank=True, null=True)
    year = models.IntegerField(max_length=4, verbose_name='Year Established')
    homepage = models.URLField(max_length=255, 
                               help_text="Enter the URL for the fund's website.",
                               blank=True)
    fund_size = models.DecimalField(max_digits=12, 
                                    decimal_places=2,
                                    verbose_name="Fund Size",
                                    help_text="Enter the the fund's total size.",
                                    blank=True)
    fund_description = models.TextField(_("Description of fund and projects funded"))
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
    slug = models.SlugField(max_length=255, editable=False)
    notes = models.TextField(_('internal notes'), blank=True)

    def project_contact1_details(self):
        if not self.project_contact1_firstname:
            return None
        name = u'%s %s' % (self.project_contact1_firstname, self.project_contact1_lastname)
        if self.project_contact1_title:
            name += u', %s' % self.project_contact1_title
        return name

    def save(self, *args, **kwargs):
        if not self.slug:
          unique_slugify(self, '%s' % (self.institution.name))
          
        super(GreenFund, self).save()

    def __unicode__(self):
        return self.fund_name

    # this might change, but for now, green fund is abstract
    class Meta:
        abstract = True

# Student Fee Driven Funds
class StudentFeeFund(GreenFund):
    term = models.CharField(choices=TERM_CHOICES,
                        max_length=5,
                        help_text="Please select the term of this fund's fee.")
    rate_per_term = models.CharField(max_length=65,
                                     verbose_name='Rate per term', 
                                     help_text="Enter the fund's rate per term.",
                                     blank=True) 
    mandatory = models.CharField(choices=COMMITMENT_CHOICES, max_length=2,
                             help_text="Is this fund fee mandatory?",
                             blank=True)
    rate_per_summer_term = models.CharField(max_length=65,
                             verbose_name='Rate per summer term', 
                             help_text="Enter the fund's rate per summer term.",
                             blank=True)

    class Meta:
        verbose_name = 'student fee driven fund'

# Donation Driven Funds
class DonationFund(GreenFund):
    fund_type = models.CharField(choices=TYPE_CHOICES, max_length=2,
                                help_text="Is this fund fee mandatory?")
    donation_source = models.CharField(choices=SOURCE_CHOICES, max_length=2,
                                help_text="Primary funding source.")

    class Meta:
        verbose_name = 'donation driven fund'

# Department Driven Funds
class DepartmentFund(GreenFund):
    department_name = models.CharField(blank=False, max_length=255,
                                    verbose_name='Department or Center Name')

    class Meta:
        verbose_name = 'department or center driven fund'