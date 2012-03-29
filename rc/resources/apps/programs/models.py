from gettext import gettext as _
from django.db import models
from rc.resources.models import ResourceItem


class Program(ResourceItem):
    type = models.ForeignKey('ProgramType', verbose_name='program type')

    class Meta:
        verbose_name = 'general program'
        verbose_name_plural = 'general programs'

class ProgramType(models.Model):
    type = models.CharField(_("type of program"), max_length=128)

    class Meta:
        verbose_name = 'program type'
        verbose_name_plural = 'program types'
        ordering = ('type',)

    def __unicode__(self):
        return self.type
