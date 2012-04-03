from django.conf.urls.defaults import patterns, include, url

from rc.resources.views import ResourceItemListView
from rc.resources.apps.operations import models


HIDE_RESOURCES_WITH_NO_ORGANIZATION = False


def handle_missing_organizations(qs):
    if HIDE_RESOURCES_WITH_NO_ORGANIZATION:
        qs = qs.exclude(organization=None)
    return qs

urlpatterns = patterns('',

    url(r'^resources/campus-alternative-transportation-websites',
        ResourceItemListView.as_view(
            model=models.TransportationWebsite,
            queryset=handle_missing_organizations(
                models.TransportationWebsite.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/bottled-water-elimination-and-reduction',
        ResourceItemListView.as_view(
            model=models.BottledWaterBan,
            queryset=handle_missing_organizations(
                models.BottledWaterBan.objects.order_by(
                    'type', 'organization__name'))),
        {'ban_types': dict(models.BottledWaterBan.BAN_TYPES),
         'member_only': True}),
         
    url(r'^resources/campus-building-energy-dashboards',
        ResourceItemListView.as_view(
            model=models.BuildingDashboard,
            queryset=handle_missing_organizations(
                models.BuildingDashboard.objects.order_by(
                    'partner__name', 'organization__name'))),
        {'member_only': True}),

    url(r'^resources/biodiesel-campus-fleets',
        ResourceItemListView.as_view(
            model=models.BiodieselFleet,
            queryset=handle_missing_organizations(
                models.BiodieselFleet.objects.order_by(
                    'production', 'organization__country', 
                    'organization__name'))),
        {'member_only': True,
         'production_types': dict(models.BiodieselFleet.PRODUCTION_TYPE)}),

    url(r'^resources/campus-bicycle-plans',
        ResourceItemListView.as_view(
            model=models.BicyclePlan,
            queryset=handle_missing_organizations(
                models.BicyclePlan.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-car-bans',
        ResourceItemListView.as_view(
            model=models.CarBan,
            queryset=handle_missing_organizations(
                models.CarBan.objects.order_by(
                    'type', 'organization__name'))),
        {'ban_types': dict(models.CarBan.BAN_TYPES),
         'member_only': True}),

    url(r'^resources/campus-commuter-surveys',
        ResourceItemListView.as_view(
            model=models.CommuterSurvey,
            queryset=handle_missing_organizations(
                models.CommuterSurvey.objects.order_by(
                    'type', 'organization__name'))),
        {'survey_types': dict(models.CommuterSurvey.SURVEY_TYPES),
         'member_only': True}),

    url(r'^resources/campus-electric-vehicle-fleets',
        ResourceItemListView.as_view(
            model=models.ElectricFleet,
            queryset=handle_missing_organizations(
                models.ElectricFleet.objects.order_by(
                    'organization__country', 'organization__name'))),
        {'member_only': True}),
         
    url(r'^resources/campus-energy-plans',
        ResourceItemListView.as_view(
            model=models.EnergyPlan,
            queryset=handle_missing_organizations(
                models.EnergyPlan.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),
         
    url(r'^resources/campus-global-warming-commitments',
        ResourceItemListView.as_view(
            model=models.GlobalWarmingCommitment,
            queryset=handle_missing_organizations(
                models.GlobalWarmingCommitment.objects.order_by(
                    'organization__name')))),

    url(r'^resources/campus-hybrid-vehicle-fleets',
        ResourceItemListView.as_view(
            model=models.HybridFleet,
            queryset=handle_missing_organizations(
                models.HybridFleet.objects.order_by(
                    'organization__country', 'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-recycling-and-waste-minimization-websites',
        ResourceItemListView.as_view(
            model=models.RecyclingWebsite,
            queryset=handle_missing_organizations(
                models.RecyclingWebsite.objects.order_by(
                    'organization__name'))),
            {'member_only': True}),
        
    url(r'^resources/energy-conservation-policies',
        ResourceItemListView.as_view(
            model=models.EnergyPolicy,
            queryset=handle_missing_organizations(
                models.EnergyPolicy.objects.order_by(
                    'organization__name')))),
        
    url(r'^resources/campus-water-conservation-efforts',
        ResourceItemListView.as_view(
            model=models.WaterConservationEffort,
            queryset=handle_missing_organizations(
                models.WaterConservationEffort.objects.order_by(
                    'organization__country', 'organization__name'))),
        {'member_only': True}),

    url(r'^resources/wind-power-campus-1',
        ResourceItemListView.as_view(
            model=models.WindTurbine,
            queryset=handle_missing_organizations(
                models.WindTurbine.objects.order_by(
                    'organization__country', 'organization__name'))),
        {'member_only': True}),

    url(r'^resources/carsharing-campus',
        ResourceItemListView.as_view(
            model=models.CarShare,
            queryset=handle_missing_organizations(
                models.CarShare.objects.order_by(
                    'partner__name', 'organization__name'))),
        {'member_only': True}),

    url(r'^resources/renewable-energy-research-centers',
        ResourceItemListView.as_view(
            model=models.RenewableResearchCenter,
            queryset=handle_missing_organizations(
                models.RenewableResearchCenter.objects.order_by(
                    'organization__name'))),
            {'member_only': True}),                    

    url(r'^resources/campus-installations-stationary-fuel-cells',
        ResourceItemListView.as_view(
            model=models.FuelCell,
            queryset=handle_missing_organizations(
                models.FuelCell.objects.order_by('-size', 
                                                 'organization__name')))),

    url(r'^resources/sustainable-dining-initiatives-campus',
        ResourceItemListView.as_view(
            model=models.DiningInitiative,
            queryset=handle_missing_organizations(
                models.DiningInitiative.objects.order_by(
                    'ownership', 'organization__name'))),
        {'owners': dict(models.DiningInitiative.OWNERS),
         'member_only': True}),

    url(r'^resources/sustainable-landscaping-campus',
        ResourceItemListView.as_view(
            model=models.SustainableLandscape,
            queryset=handle_missing_organizations(
                models.SustainableLandscape.objects.order_by(
                    'organization__name')))),

    url(r'^resources/links-related-sustainable-purchasing-campus',
        ResourceItemListView.as_view(
            model=models.PurchasingLink,
            queryset=handle_missing_organizations(
                models.PurchasingLink.objects.order_by(
                    'type', 'organization__name'))),
        {'type_list': dict(models.PurchasingLink.LINK_TYPES),
         'member_only': True}),

    url(r'^resources/campus-universal-transit-passes',
        ResourceItemListView.as_view(
            model=models.TransitPass,
            queryset=handle_missing_organizations(
                models.TransitPass.objects.order_by(
                    '-type', 'organization__country', 
                    'organization__name'))),
           {'type_list': dict(models.TransitPass.PASS_TYPES)}),
         
    )

