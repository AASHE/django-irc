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

    )

