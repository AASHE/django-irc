'''
This app encapsulates models related to the policies
pages in the AASHE resource center.
'''
from gettext import gettext as _
from django.db import models
from django.core.urlresolvers import reverse
from rc.resources.models import ResourceItem


class Policy(ResourceItem):
    '''
    Generic policy model used throughout the resource center for
    policy resources that do not require extra fields.
    '''
    type = models.ForeignKey('PolicyType', verbose_name='policy type',
                             null=True, blank=True)
    category = models.CharField(_("category"), max_length=128,
                                null=True, blank=True)

    class Meta:
        verbose_name = 'general policy'
        verbose_name_plural = 'general policies'

class PolicyType(models.Model):
    type = models.CharField(_("type of policy"), max_length=128)

    class Meta:
        verbose_name = 'policy type'
        verbose_name_plural = 'policy types'
        ordering = ('type',)

    def __unicode__(self):
        return self.type

class GreenBuildingPolicy(Policy):
    '''
    Green building policies require a LEED level field.
    '''
    LEED_LEVELS = (('PL', 'LEED Platinum'),
                   ('GL', 'LEED Gold'),
                   ('SL', 'LEED Silver'),
                   ('BZ', 'LEED Bronze'),
                   ('CR', 'LEED Certified'),
                   ('OT', 'Other Standards and Guidelines'))

    leed_level = models.CharField(max_length=2, choices=LEED_LEVELS)

    class Meta:
        verbose_name = 'green building policy'
        verbose_name_plural = 'green building policies'

class FairTradePolicy(Policy):
    '''
    Fair trade practices and policies.
    '''
    product_types = models.CharField(_('types of products'), blank=True,
                                     max_length=128)

    class Meta:
        verbose_name = 'campus fair trade practice & policy'
        verbose_name_plural = 'campus fair trade practices & policies'

class ResponsibleInvestmentPolicy(Policy):
    '''
    Socially responsible investment policies.
    '''
    investment_type = models.CharField(_('types of investment'), blank=True,
                                       max_length=128)

    class Meta:
        verbose_name = 'socially responsible investment policy'
        verbose_name_plural = 'socially responsible investment policies'

class ElectronicWastePolicy(Policy):
    items = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'electronic waste policy'
        verbose_name_plural = 'electronic waste policies'
