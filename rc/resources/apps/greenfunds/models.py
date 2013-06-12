from gettext import gettext as _
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from aashe.organization.models import Organization
from aashe.departments.models import Department
from aashe.utils.slugify import unique_slugify

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
# Student Types
STUDENT_CHOICES = (
    ('UG', 'Undergraduate'),
    ('GR', 'Graduate'),
)

# Generic Green Fund
class GreenFund(models.Model):
    fund_name = models.CharField(_('fund name'), max_length=255)
    institution = models.ForeignKey("organization.Organization",
                                  help_text="Select the institution or organization that administers this fund",
                                  )
    # Reference to fund data
    # content_type = models.ForeignKey(ContentType, blank=False, null=False)
    # object_id = models.PositiveIntegerField()
    # fund_data = generic.GenericForeignKey('content_type', 'object_id')
    year = models.IntegerField(max_length=4, verbose_name='Year Implemented')
    homepage = models.URLField(max_length=255,
                               help_text="Enter the URL for the fund's website.",
                               blank=True)
    fund_size = models.DecimalField(max_digits=12,
                                    decimal_places=2,
                                    verbose_name="Fund Size",
                                    help_text="Enter the the fund's total size.",
                                    blank=True,
                                    null=True)
    fund_description = models.TextField(_("Description of fund and projects funded"))
    fund_recipients = models.ManyToManyField("FundRecipient",
                                    help_text="Select the recipient(s) of this fund.")
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
          unique_slugify(self, '%s' % (self.fund_name))

        super(GreenFund, self).save()

    def get_fund_type_display(self):
        '''
        A special display function for use in templates
        to output what "type" of fund this is...
        '''
        return self.fund_data._meta.verbose_name

    def __unicode__(self):
        return self.fund_name

# Student Fee Driven Funds
class StudentFeeFund(GreenFund):
    sunset_date = models.DateField(blank=True,
                                null=True,
                                help_text="If this fund has a sunset date, \
                                           enter it here.")
    term = models.CharField(choices=TERM_CHOICES,
                        max_length=5,
                        help_text="Please select the term of this fund's fee.")
    rate_per_term = models.CharField(max_length=65,
                                     verbose_name='Rate per term',
                                     help_text="Enter the fund's rate per term.",
                                     blank=True)
    student_type = models.CharField(choices=STUDENT_CHOICES,
                        max_length=5,
                        help_text="Please select the student type of this fee.")

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
    department_type = models.ForeignKey("departments.Department")

    class Meta:
        verbose_name = 'department or center driven fund'

# Hybrid Funds
class HybridFund(GreenFund):
    funding_source = models.TextField(_("Description of funding source"))

    def __unicode__(self):
        return self.funding_source

    class Meta:
        verbose_name = 'hybrid green fund'

class FundRecipient(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'fund recipient type'
