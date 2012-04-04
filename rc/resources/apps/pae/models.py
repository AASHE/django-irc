from gettext import gettext as _
from django.db import models
from rc.resources.models import ResourceItem


class AssessmentTool(ResourceItem):
    CREATORS = (('AA', 'Assessment Tools from AASHE'),
                ('OT', 'Assessment Tools from Other Organizations'))
    provider = models.CharField(_('tool provider'), choices=CREATORS,
                                max_length=2, default='AA')
    
    class Meta:
        verbose_name = 'campus sustainability assessment tool'

class MasterPlan(ResourceItem):
    minor_reference_only = models.BooleanField(_('minor reference only'),
                                               default=False)

    class Meta:
        verbose_name = 'campus master plan'

class SustainabilityWebsite(ResourceItem):
    class Meta:
        verbose_name = 'campus sustainability website'

class SustainabilityBlog(ResourceItem):
    class Meta:
        verbose_name = 'campus sustainability blog'

class SustainabilityPlan(ResourceItem):
    class Meta:
        verbose_name = 'campus sustainability plan'

class AlumniFund(ResourceItem):
    class Meta:
        verbose_name = 'alumni sustainability fund'

class RevolvingLoanFund(ResourceItem):
    class Meta:
        verbose_name = 'revolving loan fund'

class StudentFee(ResourceItem):
    class Meta:
        verbose_name = 'student fee for sustainability'
        verbose_name_plural = 'student fees for sustainability'

