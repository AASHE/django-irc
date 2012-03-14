from django.contrib import admin
from rc.resources.apps.operations.models import *


class BottledWaterBanAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'type', 'published')
    list_filter = ('type',)
admin.site.register(BottledWaterBan, BottledWaterBanAdmin)

class CarShareAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'partner')
    list_filter = ('partner',)
admin.site.register(CarShare, CarShareAdmin)
    
admin.site.register(GreenBuildingWebsite)
admin.site.register(CampusGreenBuilding)
admin.site.register(GreenBuildingType)
admin.site.register(ClimateActionPlan)
admin.site.register(CAPPublication)
admin.site.register(GlobalWarmingCommitment)
admin.site.register(GHGInventory)
admin.site.register(DiningInitiative)
admin.site.register(BuildingDashboard)
admin.site.register(BuildingDashboardPartner)
admin.site.register(FuelCell)
admin.site.register(RenewableResearchCenter)
admin.site.register(EnergyWebsite)
admin.site.register(EnergyPlan)
admin.site.register(EnergyPolicy)
admin.site.register(WindTurbine)
admin.site.register(SustainableLandscape)
admin.site.register(PurchasingLink)
admin.site.register(TransportationWebsite)
admin.site.register(BicyclePlan)
admin.site.register(CarBan)
admin.site.register(CommuterSurvey)
admin.site.register(BiodieselFleet)
admin.site.register(ElectricFleet)
admin.site.register(HybridFleet)
admin.site.register(CarSharePartner)
admin.site.register(TransitPass)
admin.site.register(RecyclingWebsite)
admin.site.register(WaterConservationEffort)

