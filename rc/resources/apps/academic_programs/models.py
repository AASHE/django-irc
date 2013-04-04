from gettext import gettext as _
from django.db import models
from geopy import geocoders
from aashe.organization.models import Organization
from aashe.disciplines.models import Discipline
from aashe.utils.slugify import unique_slugify

# Commitment
COMMITMENT_CHOICES = (
    ('FT', 'Full-time'),
    ('PT', 'Part-time'),
    ('BT', 'Both')
)
# Distance Ed
DISTANCE_CHOICES = (
    ('LO', 'Local-only'),
    ('DT', 'Distance-education'),
    ('BT', 'Both')
)

# Create your models here.
class AcademicProgram(models.Model):
    title = models.CharField(_('program name'), max_length=255)
    institution = models.ForeignKey("organization.Organization", 
                                  help_text="Select the institution or organization that offer this program \
                                  If you need to list more, use the space below.", blank=True, null=True)
    other_inst = models.TextField(_('other institutions'), 
                                  help_text='List any institutions not found in the above list.', blank=True)
    description = models.TextField(verbose_name='Program Description', 
                                   help_text="Briefly describe the program in 500 words or less.", blank=True)
    location_name = models.CharField(max_length=255, 
                                     help_text="e.g. a campus or place of business", blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=6, verbose_name='State/Province',
                             help_text='Two character abbreviation', blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    country = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, editable=False)
    program_type = models.ForeignKey("ProgramType")
    homepage = models.URLField(max_length=255, 
                               help_text="Enter the URL for the program's website.")
    department = models.CharField(max_length=200, 
                                  help_text="Enter the full name(s) of the department(s) that administer this program, if applicable.",
                                  blank=True)
    duration = models.CharField(max_length=255, 
                                help_text='Enter the amount of time typically required to complete this \
                                program (e.g. "4 years with summers off", "2 years with a summer project \
                                between years 1 and 2", "3 months", or "1 week").', blank=True)
    founded = models.CharField(max_length=200, verbose_name='Year Founded',
                             help_text='Enter the year (YYYY) in which the program was created.', blank=True)
    distance_ed = models.CharField(choices=DISTANCE_CHOICES,
                                         max_length=5,
                                         help_text='Is this a distance education program?')
    commitment = models.CharField(choices=COMMITMENT_CHOICES,
                                         max_length=5,
                                         help_text='Is this program full time, part-time, or both?')
    language = models.CharField(max_length=150,
                                help_text="What is this program's primary language of instruction?",
                                blank=True)
    blog = models.URLField(max_length=300, 
                           help_text="Enter the URL for the program's blog, if applicable.",
                           blank=True)
    linkedin = models.URLField(max_length=300, 
                               help_text="Enter the URL for the program's LinkedIn page, if applicable.",
                               blank=True)
    facebook = models.URLField(max_length=300, 
                               help_text="Enter the URL for the program's Facebook page, if applicable.",
                               blank=True)
    twitter = models.URLField(max_length=300,
                              help_text="Enter the URL for the program's Twitter page, if applicable.",
                              blank=True)
    discipline = models.ForeignKey("disciplines.Discipline", 
                                   help_text="Select the discipline or field that best describes \
                                   the approach and focus of this program.")
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
            # create a slug
            if not self.slug:
              unique_slugify(self, '%s' % (self.title))
            # if there's no city, state, or country given, use the institution's
            if not self.city:
              try:
                self.city = self.institution.city
              except:
                pass
            if not self.state:
              try:
                if self.institution.state.__len__() < 7:
                  self.state = self.institution.state
              except:
                pass
            if not self.country:
              try:
                self.country = self.institution.country
              except:
                pass
            # hacky data cleaning
            if self.country == "United States" or "USA":
              self.country = "United States of America"
            if self.city and self.state:
              # geolocate lat and long
              g = geocoders.Google()
              location = "%s %s" % (self.city, self.state)
              try:
                place, (lat, lng) = g.geocode(location)
                self.latitude = lat
                self.longitude = lng
              except:
                # try for multiple locations
                try:
                  for place, (lat, lng) in g.geocode(location, exactly_one=False):
                    self.latitude = lat
                    self.longitude = lng
                except:
                  pass
              
            super(AcademicProgram, self).save()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "academic program"

class ProgramType(models.Model):
    name = models.CharField(_('type name'), max_length=255)
    slug = models.CharField(_('type code'), max_length=100)
    
    def __unicode__(self):
        return self.name

    