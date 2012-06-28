from django.contrib import admin
from rc.resources.admin import ResourceItemAdmin
from rc.resources.apps.operations.models import *


class BottledWaterBanAdmin(ResourceItemAdmin):
    list_filter = ('type', 'published',)
admin.site.register(BottledWaterBan, BottledWaterBanAdmin)

class CarShareAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'partner')
    list_filter = ('partner',)
admin.site.register(CarShare, CarShareAdmin)

admin.site.register(ElectronicWasteEvent, ResourceItemAdmin)
admin.site.register(GreenBuildingWebsite, ResourceItemAdmin)
admin.site.register(GreenBuildingType)
admin.site.register(ClimateActionPlan, ResourceItemAdmin)
admin.site.register(CAPPublication, ResourceItemAdmin)
admin.site.register(GlobalWarmingCommitment, ResourceItemAdmin)
admin.site.register(GHGInventory, ResourceItemAdmin)
admin.site.register(DiningInitiative, ResourceItemAdmin)
admin.site.register(BuildingDashboard, ResourceItemAdmin)
admin.site.register(BuildingDashboardPartner)
admin.site.register(FuelCell, ResourceItemAdmin)
admin.site.register(RenewableResearchCenter, ResourceItemAdmin)
admin.site.register(EnergyWebsite, ResourceItemAdmin)
admin.site.register(EnergyPlan, ResourceItemAdmin)
admin.site.register(EnergyPolicy, ResourceItemAdmin)
admin.site.register(WindTurbine, ResourceItemAdmin)
admin.site.register(SustainableLandscape, ResourceItemAdmin)
admin.site.register(PurchasingLink, ResourceItemAdmin)
admin.site.register(TransportationWebsite, ResourceItemAdmin)
admin.site.register(BicyclePlan, ResourceItemAdmin)
admin.site.register(CarBan, ResourceItemAdmin)
admin.site.register(CommuterSurvey, ResourceItemAdmin)
admin.site.register(BiodieselFleet, ResourceItemAdmin)
admin.site.register(ElectricFleet, ResourceItemAdmin)
admin.site.register(HybridFleet, ResourceItemAdmin)
admin.site.register(CarSharePartner)
admin.site.register(TransitPass, ResourceItemAdmin)
admin.site.register(RecyclingWebsite, ResourceItemAdmin)
admin.site.register(WaterConservationEffort, ResourceItemAdmin)

class CampusGreenBuildingAdmin(ResourceItemAdmin):
    exclude = ('title',)
    list_display = ('facility_name', 'organization', 'notes', 'url', 'published')
    list_filter = ('type', 'published')
admin.site.register(CampusGreenBuilding, CampusGreenBuildingAdmin)
admin.site.register(GreenResidenceHall, ResourceItemAdmin)
admin.site.register(CampusGreenBuildingLink)


