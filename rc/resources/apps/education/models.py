from gettext import gettext as _
from django.db import models
from rc.resources.models import ResourceItem


class CommunityGarden(ResourceItem):
    class Meta:
        verbose_name = 'campus and campus-community garden'

class SustainabilityNetworks(ResourceItem):
    class Meta:
        verbose_name = 'alumni sustainability network'

class CampusAgriculture(ResourceItem):
    class Meta:
        ordering = ('title',)
        verbose_name = 'campus supported agriculture and farms'
        verbose_name_plural = 'campus supported agriculture and farms'

class LivingGuides(ResourceItem):
    class Meta:
        ordering = ('title',)
        verbose_name = 'campus sustainable living guide'

class SustainabilityMaps(ResourceItem):
    class Meta:
        verbose_name = 'campus sustainability map/tour'
        verbose_name_plural = 'campus sustainability maps/tours'

class StudentPeerOutreach(ResourceItem):
    # TODO: Add fields
    class Meta:
        verbose_name = 'peer to peer sustainability outreach campaign'

class CampusSustainabilityCourse(ResourceItem):
    department_number = models.CharField(_('department and number'), max_length=75)
    faculty_first_name = models.CharField(_('faculty first name'), max_length=75)
    faculty_last_name = models.CharField(_('faculty last name'), max_length=75)
    faculty_title = models.CharField(_('faculty title'), max_length=75)
    faculty_dept = models.CharField(_('faculty department'), max_length=75)
    faculty_email = models.CharField(_('faculty email'), max_length=75)
    
    class Meta:
        verbose_name = 'course on campus sustainability'
        verbose_name_plural = 'courses on campus sustainability'
        
class SustainabilityCourseInventory(ResourceItem):
    class Meta:
        ordering = ('title',)
        verbose_name = 'sustainability course inventory'
        verbose_name_plural = 'sustainability course inventories'

class SustainabilitySyllabus(ResourceItem):
    class Meta:
        ordering = ('title',)
        verbose_name = 'sustainability-related syllabus'
        verbose_name_plural = 'sustainability-related syllabi'

class FacultyWorkshops(ResourceItem):
    class Meta:
        verbose_name = 'faculty development workshop'

class SurveyOfAwareness(ResourceItem):
    class Meta:
        verbose_name = 'survey of sustainability awareness, attitudes, and values'
        verbose_name_plural = 'surveys of sustainability awareness, attitudes, and values'

class ResearchInventories(ResourceItem):
    class Meta:
        verbose_name = 'sustainability research inventory'
        verbose_name_plural = 'sustainability research inventories'

class AcademicCenter(ResourceItem):
    type = models.ForeignKey('AcademicCenterType', verbose_name='academic center type')
    
    class Meta:
        verbose_name = 'academic center on sustainability'
        verbose_name_plural = 'academic centers on sustainability'

class AcademicCenterType(models.Model):
    type = models.CharField(_('academic center type'), max_length=75)
    
    class Meta:
        verbose_name = 'academic center type'
        
