from gettext import gettext as _
from django.db import models
from rc.resources.models import ResourceItem
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

def academic_centers_url_name(center_type_code):
    academic_center_types = dict(AcademicCenterType.CENTER_TYPES)
    return 'academic-centers-' + slugify(academic_center_types[center_type_code])

class CommunityGarden(ResourceItem):
    class Meta:
        verbose_name = 'campus and campus-community garden'
        
    def get_absolute_url(self):
        return reverse('community-gardens')

class StudyAbroadProgram(ResourceItem):
    PROGRAM_TYPES = (('IN', 'Institutions Offering Study Abroad Programs in Sustainability'),
                ('OT', 'Organizations Offering Sustainability Study Abroad Programs'))

    type = models.CharField(_('program type'), max_length=2,
                            choices=PROGRAM_TYPES, blank=False)

    class Meta:
        verbose_name = 'campus sustainability study abroad program'
        verbose_name_plural = 'campus sustainability study abroad programs'
        
    def get_absolute_url(self):
        return reverse('study-abroad-programs')

class SustainabilityNetwork(ResourceItem):
    class Meta:
        verbose_name = 'alumni sustainability network'
    
    def get_absolute_url(self):
        return reverse('sustainability-networks')

class CampusAgriculture(ResourceItem):
    class Meta:
        ordering = ('title',)
        verbose_name = 'campus supported agriculture and farms'
        verbose_name_plural = 'campus supported agriculture and farms'
        
    def get_absolute_url(self):
        return reverse('campus-agricultures')

class LivingGuide(ResourceItem):
    class Meta:
        ordering = ('title',)
        verbose_name = 'campus sustainable living guide'
        
    def get_absolute_url(self):
        return reverse('living-guides')

class SustainabilityMap(ResourceItem):
    class Meta:
        verbose_name = 'campus sustainability map/tour'
        verbose_name_plural = 'campus sustainability maps/tours'
        
    def get_absolute_url(self):
        return reverse('sustainability-maps')

class StudentPeerOutreach(ResourceItem):
    # TODO: Add fields
    class Meta:
        verbose_name = 'peer to peer outreach campaign'

class CampusSustainabilityCourseTeacher(models.Model):
    first_name = models.CharField(_('faculty first name'), max_length=75)
    middle_name = models.CharField(_('faculty middle name'), max_length=75, blank=True)
    last_name = models.CharField(_('faculty last name'), max_length=75)
    title = models.CharField(_('title'), max_length=255, blank=True)
    department = models.CharField(_('faculty department'), max_length=75, blank=True)
    email = models.EmailField(('faculty email'), max_length=255, blank=True)
    web_page = models.CharField(('faculty web page'), max_length=75, blank=True)

    class Meta:
        ordering = ('last_name', 'first_name')
        verbose_name = 'course on sustainability teacher'
        verbose_name_plural = 'course on sustainability teachers'

    class Admin:
        list_display = ('last_name', 'first_name', 'title',
                        'email', 'web_page', 'department')
                        
    def __unicode__(self):
        return (self.first_name + ' ' + self.last_name)
        
    def get_absolute_url(self):
        return reverse('campus-sustainability-courses')

class CampusSustainabilityCourse(ResourceItem):
    department_number = models.CharField(_('department and number'),
                                         max_length=75, blank=True, null=True)
    teachers = models.ManyToManyField(CampusSustainabilityCourseTeacher)

    class Meta:
        ordering = ('title',)
        verbose_name = 'course on sustainability'
        verbose_name_plural = 'courses on sustainability'
        
    def get_absolute_url(self):
        return reverse('campus-sustainability-courses')

class SustainabilityCourseInventory(ResourceItem):
    class Meta:
        ordering = ('title',)
        verbose_name = 'sustainability course inventory'
        verbose_name_plural = 'sustainability course inventories'
    
    def get_absolute_url(self):
        return reverse('sustainability-course-inventories')

class SustainabilitySyllabus(ResourceItem):
    class Meta:
        ordering = ('title',)
        verbose_name = 'sustainability-related syllabus'
        verbose_name_plural = 'sustainability-related syllabi'
        
    def get_absolute_url(self):
        return reverse('sustainability-syllabi')

class FacultyWorkshop(ResourceItem):
    class Meta:
        verbose_name = 'faculty development workshop'
        
    def get_absolute_url(self):
        return reverse('faculty-workshops')

class SurveyOfAwareness(ResourceItem):
    class Meta:
        verbose_name = 'sustainability survey'
        verbose_name_plural = 'sustainability surveys'
    
    def get_absolute_url(self):
        return reverse('surveys-of-awareness')

class ResearchInventory(ResourceItem):
    class Meta:
        verbose_name = 'sustainability research inventory'
        verbose_name_plural = 'sustainability research inventories'

    def get_absolute_url(self):
        return reverse('research-inventories')

class AcademicCenter(ResourceItem):
    type = models.ForeignKey('AcademicCenterType', verbose_name='academic center type')

    class Meta:
        verbose_name = 'academic center on sustainability'
        verbose_name_plural = 'academic centers on sustainability'
    
    def get_absolute_url(self):
        return reverse(academic_centers_url_name(self.type.type))

class AcademicCenterType(models.Model):
    CENTER_TYPES = (('AG', 'Agriculture'),
                    ('AR', 'Architecture'),
                    ('BS', 'Business'),
                    ('DS', 'Development Studies'),
                    ('EC', 'Economics'),
                    ('ED', 'Education'),
                    ('EN', 'Engineering'),
                    ('LW', 'Law'),
                    ('US', 'Urban Studies'))

    type = models.CharField(_('academic center type'), max_length=2,
                            choices=CENTER_TYPES, blank=True)

    class Meta:
        verbose_name = 'academic center type'
        verbose_name_plural = 'academic center types'

    def __unicode__(self):
        return self.get_type_display()
