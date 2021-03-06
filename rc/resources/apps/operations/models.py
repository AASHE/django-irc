# coding=utf8
from gettext import gettext as _
from django.db import models
from rc.resources.models import ResourceItem
from django.core.urlresolvers import reverse

class GreenBuildingWebsite(ResourceItem):
    class Meta:
        verbose_name = 'website on campus green building'
        verbose_name_plural = 'websites on campus green building'

class CampusGreenBuilding(ResourceItem):
    LEED_LEVELS = (('AP', 'LEED Platinum'),
                    ('BG', 'LEED Gold'),
                    ('CS', 'LEED Silver'),
                    ('DB', 'LEED Bronze'),
                    ('EC', 'LEED Certified'),
                    ('FC', 'Other Certification'),
                    ('GN', 'Non-Certified or Certification Unknown'))
    
    type = models.ForeignKey('GreenBuildingType', verbose_name='building type')
    facility_name = models.CharField(_('facility name'), max_length=128, blank=False)
    completed = models.CharField(_('when completed'), max_length=128, blank=True)
    sqft = models.CharField(_('square footage'), max_length=56, blank=True)
    cost = models.CharField(_('building cost'), max_length=56, blank=True)
    certification = models.CharField(_('certification'), choices=LEED_LEVELS, max_length=128)
    key_features = models.TextField(_('key features'), blank=True)

    class Meta:
        verbose_name = 'green building on campus'
        verbose_name_plural = 'green buildings on campus'
    
    def __unicode__(self):
      return self.facility_name

class CampusGreenBuildingLink(models.Model):
    '''CampusGreenBuildings can have a number of links.  These are
    represented by CampusGreenBuildingLinks.
    '''
    title = models.CharField(_('resource title'), max_length=256)
    url = models.URLField(_('resource url'), blank=True, max_length=256)
    resource_item = models.ForeignKey(CampusGreenBuilding,
                                      related_name='links')
                                      
    def __unicode__(self):
      return self.title

class GreenResidenceHall(CampusGreenBuilding):
    beds = models.CharField(_('beds'), blank=True, max_length=56)

class GreenBuildingType(models.Model):
    type = models.CharField(_('campus green building type'), max_length=75)

    class Meta:
        verbose_name = 'green building type'

    def __unicode__(self):
        return self.type

class ClimateActionPlan(ResourceItem):
    class Meta:
        verbose_name = 'campus climate action plan'

class CAPPublication(ResourceItem):
    class Meta:
        verbose_name = 'publication on campus climate action'
        verbose_name_plural = 'publications on campus climate action'

class GlobalWarmingCommitment(ResourceItem):
    commitment = models.CharField(_('commitment (ex: 20% by 2050)'), max_length=128)
    date = models.DateField(_('date of commitment'), blank=True, null=True)

    class Meta:
        verbose_name = 'campus global warming commitment'
    
    def __unicode__(self):
        return self.commitment
    
    def get_absolute_url(self):
        return reverse("global-warming-commitments")

class GHGInventory(ResourceItem):
    METHODOLOGY_TYPES = (('CA', 'Clean Air-Cool Planet Campus Carbon Calculator'),
                         ('CR', 'California Climate Action Registry'),
                         ('TS', 'Torrie Smith Associates emission Greenhouse Gas Strategy Software'),
                         ('OT', 'Individually-Derived and Other Methodologies'))

    methodology = models.CharField(_('methodology or tool'),
                                   choices=METHODOLOGY_TYPES, max_length=2)

    class Meta:
        verbose_name = 'campus ghg inventory'
        verbose_name_plural = 'campus ghg inventories'

class DiningInitiative(ResourceItem):
    OWNERS = (('SO', u'Self-Operated'),
              ('AK', u'Aramark'),
              ('BA', u'Bon Appétit'),
              ('CW', u'Chartwells'),
              ('SX', u'Sodexo'))
    ownership = models.CharField(_('ownership of operation'),
                                 choices=OWNERS, max_length=2)

    class Meta:
        verbose_name = 'sustainable dining initiative'
        verbose_name_plural = 'sustainable dining initiatives'
        
    def get_absolute_url(self):
        return reverse("dining-initiatives")

class BuildingDashboard(ResourceItem):
    partner = models.ForeignKey('BuildingDashboardPartner',
                                verbose_name='building energy dashboard partner',
                                help_text="Leave blank for 'individually developed'",
                                blank=True, null=True)

    class Meta:
        verbose_name = 'building energy dashboard'
        verbose_name_plural = 'building energy dashboards'
        
    def get_absolute_url(self):
        return reverse("building-dashboards")

class BuildingDashboardPartner(models.Model):
    name = models.CharField(_('partner name'), max_length=128)

    class Meta:
        verbose_name = 'building energy dashboard partner'
        verbose_name_plural = 'building energy dashboard partners'

    def __unicode__(self):
        return self.name

class FuelCell(ResourceItem):
    size = models.DecimalField(_('system size (kW)'), max_digits=6,
                                 decimal_places=1)
    class Meta:
        verbose_name = 'stationary fuel cell'
    
    def get_absolute_url(self):
        return reverse("fuel-cells")

class RenewableResearchCenter(ResourceItem):
    class Meta:
        verbose_name = 'renewable energy research center'
        
    def get_absolute_url(self):
        return reverse("renewable-research-centers")

class EnergyWebsite(ResourceItem):
    class Meta:
        verbose_name = 'campus energy website'
        
    def get_absolute_url(self):
        return reverse("energy-websites")

class EnergyPlan(ResourceItem):
    date_published = models.DateField(_('date published'), blank=True, null=True)

    class Meta:
        verbose_name = 'campus energy plan'
        
    def get_absolute_url(self):
        return reverse("energy-plans")

class EnergyPolicy(ResourceItem):
    class Meta:
        verbose_name = 'campus sustainable energy policy'
        verbose_name_plural = 'campus sustainable energy policies'

class WindTurbine(ResourceItem):
    size = models.DecimalField(_('system size (kW)'), max_digits=6,
                               decimal_places=1,
                               blank=True, null=True)

    class Meta:
        verbose_name = 'campus wind turbine'
        
    def get_absolute_url(self):
        return reverse("wind-turbines")

class SustainableLandscape(ResourceItem):
    class Meta:
        verbose_name = 'sustainable landscaping'
        verbose_name_plural = 'sustainable landscaping'
    
    def get_absolute_url(self):
        return reverse("sustainable-landscapes")
            
class PurchasingLink(ResourceItem):
    LINK_TYPES = (('CA', 'Campus Links'),
                  ('OT', 'Other Links'))
    type = models.CharField(_('link type'), choices=LINK_TYPES,
                            max_length=2)

    class Meta:
        verbose_name = 'sustainable purchasing link'
        verbose_name_plural = 'sustainable purchasing links'
        
    def get_absolute_url(self):
        return reverse("purchasing-links")

class TransportationWebsite(ResourceItem):
    class Meta:
        verbose_name = 'alternative transportation website'
    
    def get_absolute_url(self):
        return reverse("transportation-websites")

class BicyclePlan(ResourceItem):
    class Meta:
        verbose_name = 'campus bicycle plan'
        
    def get_absolute_url(self):
        return reverse("bicycle-plans")

class CarBan(ResourceItem):
    BAN_TYPES = (('FY', 'First Year Student Car Bans'),
                 ('EX', 'Extended Car Bans'))
    type = models.CharField(_('ban type'), choices=BAN_TYPES,
                            max_length=2)

    class Meta:
        verbose_name = 'campus car ban'
        
    def get_absolute_url(self):
        return reverse("car-bans")

class CommuterSurvey(ResourceItem):
    SURVEY_TYPES = (('SE', 'Survey Examples'),
                    ('SR', 'Survey Results/Analysis Examples'),
                    ('RG', 'Rules and Guidelines for Gathering Information'))
    type = models.CharField(_('survey type'), choices=SURVEY_TYPES,
                            max_length=2)

    class Meta:
        verbose_name = 'campus commuter survey'
        
    def get_absolute_url(self):
        return reverse("commuter-surveys")

class BiodieselFleet(ResourceItem):
    PRODUCTION_TYPE = (('CP', 'Campus-Produced Biodiesel in Campus Fleets'),
                       ('PB', 'Purchased Biodiesel in Campus Fleets'))
    production = models.CharField(_('production category'),
                                  choices=PRODUCTION_TYPE,
                                  max_length=2,
                                  blank=True)
    type = models.CharField(_('biodiesel type (B20, B50, etc)'), max_length=30,
                            blank=True)

    class Meta:
        verbose_name = 'campus biodiesel fleet'
        
    def get_absolute_url(self):
        return reverse("biodiesel-fleets")

class ElectricFleet(ResourceItem):
    number = models.IntegerField(_('number of vehicles'), blank=True, null=True)

    class Meta:
        verbose_name = 'campus electric vehicle fleet'
        
    def get_absolute_url(self):
        return reverse("electric-fleets")

class ElectronicWasteEvent(ResourceItem):

    class Meta:
        verbose_name = 'electronic waste event'

class HybridFleet(ResourceItem):
    number = models.IntegerField(_('number of vehicles'), blank=True, null=True)

    class Meta:
        verbose_name = 'campus hybrid vehicle fleet'
    
    def get_absolute_url(self):
        return reverse("hybrid-fleets")

class CarShare(ResourceItem):
    partner = models.ForeignKey('CarSharePartner',
                                verbose_name='car share partner')

    class Meta:
        ordering = ('title',)
        verbose_name = 'car share'
        verbose_name_plural = 'car sharing'
        
    def get_absolute_url(self):
        return reverse("car-shares")

class CarSharePartner(models.Model):
    name = models.CharField(_('partner name'), max_length=64)

    class Meta:
        ordering = ('name',)
        verbose_name = 'car share partner'
        verbose_name_plural = 'car share partners'

    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("car-shares")

class TransitPass(ResourceItem):
    PASS_TYPES = (('UP', 'Universal Bus/Transit Pass Programs'),
                  ('BD', 'Bus/Transit Pass Discount Programs'))
    type = models.CharField(_('transit pass type'), choices=PASS_TYPES,
                            max_length=2)

    class Meta:
        verbose_name = 'universal access transit pass'
        verbose_name_plural = 'universal access transit passes'
        
    def get_absolute_url(self):
        return reverse("transit-passes")

class BottledWaterBan(ResourceItem):
    BAN_TYPES = (('CW', 'Campus-Wide Bans'),
                 ('AS', 'Area, School and Department Specific Bans'),
                 ('SB', 'Student Campaigns to Ban Bottled Water'),
                 ('AR', 'Awareness and Reduction Campaigns'))
    type = models.CharField(_('reduction type'), max_length=2,
                            choices=BAN_TYPES, blank=True)

    class Meta:
        ordering = ('title',)
        verbose_name = 'bottled water reduction'
        verbose_name_plural = 'bottled water reductions'
    
    def get_absolute_url(self):
        return reverse("bottled-water-bans")

class RecyclingWebsite(ResourceItem):
    class Meta:
        verbose_name = 'campus recycling/waste website'
    
    def get_absolute_url(self):
        return reverse("recycling-websites")

class WaterConservationEffort(ResourceItem):
    class Meta:
        verbose_name = 'campus water conservation effort'
    
    def get_absolute_url(self):
        return reverse("water-conservation-efforts")
