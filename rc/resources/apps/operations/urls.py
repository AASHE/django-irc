from django.conf.urls.defaults import patterns, url
from django.template.defaultfilters import slugify

from rc.resources.views import ResourceItemListView
from rc.resources.apps.operations import models

from aashe.aasheauth.decorators import members_only


def green_building_url(url_string, building_type, image_url=None,
                       image_alt=None, image_caption=None,
                       buildings_name=None, model=models.CampusGreenBuilding):
    if not buildings_name:
        buildings_name = ' '.join(building_type.split()[1:]).lower()
    return url(url_string,
               members_only(ResourceItemListView.as_view(
                   model=model,
                   queryset=model.objects.filter(
                           type__type=building_type).order_by(
                               'type', 'certification', 'organization__name'),
                   template_name='operations/campusgreenbuilding_list.html')),
               name=slugify(building_type),
               kwargs={'member_only': True,
                       'cert_order': ('LEED Platinum', 'LEED Gold',
                                      'LEED Silver', 'LEED Certified',
                                      'not certified'),
                       'title': building_type,
                       'image_url': image_url,
                       'image_alt': image_alt,
                       'image_caption': image_caption,
                       'buildings_name': buildings_name})

urlpatterns = patterns('',

    url(r'^campus-alternative-transportation-websites',
        members_only(ResourceItemListView.as_view(
            model=models.TransportationWebsite,
            queryset=models.TransportationWebsite.objects.order_by(
                    'organization__name'))),
        name='transportation-websites',
        kwargs={'member_only': True, 'title': 'Campus Alternative Transportation Websites'}),

    url(r'^bottled-water-elimination-and-reduction',
        members_only(ResourceItemListView.as_view(
            model=models.BottledWaterBan,
            queryset=models.BottledWaterBan.objects.order_by(
                    'type', 'organization__name'))),
        name='bottled-water-bans',
        kwargs={'type_list': [ level[0] for level in
                               models.BottledWaterBan.BAN_TYPES ],
                'type_dict': dict(models.BottledWaterBan.BAN_TYPES),
                'title': 'Campus Bottled Water Bans and Reduction Campaigns',
                'member_only': True}),

    url(r'^campus-building-energy-dashboards',
        members_only(ResourceItemListView.as_view(
            model=models.BuildingDashboard,
            queryset=models.BuildingDashboard.objects.order_by(
                    'partner__name', 'organization__name'))),
        name='building-dashboards',
        kwargs={'title': 'Campus Building Energy Dashboards',
                'member_only': True}),

    url(r'^biodiesel-campus-fleets',
        members_only(ResourceItemListView.as_view(
            model=models.BiodieselFleet,
            queryset=models.BiodieselFleet.objects.order_by(
                    'production', 'organization__country',
                    'organization__name'))),
        name='biodiesel-fleets',
        kwargs={'member_only': True,
                'production_types':
                dict(models.BiodieselFleet.PRODUCTION_TYPE)}),

    url(r'^campus-bicycle-plans',
        members_only(ResourceItemListView.as_view(
            model=models.BicyclePlan,
            queryset=models.BicyclePlan.objects.order_by(
                    'organization__name'))),
        name='bicycle-plans',
        kwargs={'member_only': True}),

    url(r'^campus-car-bans',
        ResourceItemListView.as_view(
            model=models.CarBan,
            queryset=models.CarBan.objects.order_by(
                    '-type', 'organization__name')),
        name='car-bans',
        kwargs={'ban_types': dict(models.CarBan.BAN_TYPES)}),

    url(r'^campus-commuter-surveys',
        members_only(ResourceItemListView.as_view(
            model=models.CommuterSurvey,
            queryset=models.CommuterSurvey.objects.order_by(
                    'type', 'organization__name'))),
        name='commuter-surveys',
        kwargs={'survey_types': dict(models.CommuterSurvey.SURVEY_TYPES),
                'member_only': True}),

    url(r'^campus-electric-vehicle-fleets',
        members_only(ResourceItemListView.as_view(
            model=models.ElectricFleet,
            queryset=models.ElectricFleet.objects.order_by(
                    'organization__country', 'organization__name'))),
        name='electric-fleets',
        kwargs={'member_only': True}),

    url(r'^campus-energy-plans',
        members_only(ResourceItemListView.as_view(
            model=models.EnergyPlan,
            queryset=models.EnergyPlan.objects.order_by(
                    'organization__name'))),
        name='energy-plans',
        kwargs={'member_only': True}),

    url(r'^campus-energy-plans',
        members_only(ResourceItemListView.as_view(
            model=models.EnergyPlan,
            queryset=models.EnergyPlan.objects.order_by(
                    'organization__name'))),
        name='energy-plans',
        kwargs={'member_only': True}),

    url(r'^campus-energy-websites',
        ResourceItemListView.as_view(
            model=models.EnergyWebsite,
            queryset=models.EnergyWebsite.objects.order_by(
                    'organization__name')),
            name='energy-websites'),

    url(r'^campus-global-warming-commitments',
        ResourceItemListView.as_view(
            model=models.GlobalWarmingCommitment,
            queryset=models.GlobalWarmingCommitment.objects.order_by(
                    'organization__name', 'date')),
            name='global-warming-commitments'),

    url(r'^campus-hybrid-vehicle-fleets',
        members_only(ResourceItemListView.as_view(
            model=models.HybridFleet,
            queryset=models.HybridFleet.objects.order_by(
                    'organization__country', 'organization__name'))),
        name='hybrid-fleets',
        kwargs={'member_only': True}),

    url(r'^campus-recycling-and-waste-minimization-websites',
        members_only(ResourceItemListView.as_view(
            model=models.RecyclingWebsite,
            queryset=models.RecyclingWebsite.objects.order_by(
                    'organization__name'))),
        name='recycling-websites',
        kwargs={'member_only': True}),

    url(r'^campus-water-conservation-efforts',
        members_only(ResourceItemListView.as_view(
            model=models.WaterConservationEffort,
            queryset=models.WaterConservationEffort.objects.order_by(
                    'organization__country', 'organization__name'))),
        name='water-conservation-efforts',
        kwargs={'member_only': True}),

    url(r'^wind-power-campus-1',
        members_only(ResourceItemListView.as_view(
            model=models.WindTurbine,
            queryset=models.WindTurbine.objects.order_by(
                    '-size', 'organization__name'))),
        name='wind-turbines',
        kwargs={'member_only': True}),

    url(r'^carsharing-campus',
        members_only(ResourceItemListView.as_view(
            model=models.CarShare,
            queryset=models.CarShare.objects.order_by(
                    'partner__name', 'organization__name'))),
        name='car-shares',
        kwargs={'member_only': True}),

    url(r'^renewable-energy-research-centers',
        members_only(ResourceItemListView.as_view(
            model=models.RenewableResearchCenter,
            queryset=models.RenewableResearchCenter.objects.order_by(
                    'organization__name'))),
        name='renewable-research-centers',
        kwargs={'member_only': True}),

    url(r'^campus-installations-stationary-fuel-cells',
        ResourceItemListView.as_view(
            model=models.FuelCell,
            queryset=models.FuelCell.objects.order_by('-size',
                                                      'organization__name')),
        name='fuel-cells',
        kwargs={'title': 'Campus Installations of Stationary Fuel Cells'}),

    url(r'^sustainable-dining-initiatives-campus',
        members_only(ResourceItemListView.as_view(
            model=models.DiningInitiative,
            queryset=models.DiningInitiative.objects.order_by(
                    'ownership', 'organization__name'))),
        name='dining-initiatives',
        kwargs={'owners': dict(models.DiningInitiative.OWNERS),
                'member_only': True}),

    url(r'^sustainable-landscaping-campus',
        ResourceItemListView.as_view(
            model=models.SustainableLandscape,
            queryset=models.SustainableLandscape.objects.order_by(
                    'organization__name')),
        name='sustainable-landscapes',
        kwargs={'title': 'Sustainable Landscaping Initiatives on Campus'}),

    url(r'^links-related-sustainable-purchasing-campus',
        members_only(ResourceItemListView.as_view(
            model=models.PurchasingLink,
            queryset=models.PurchasingLink.objects.order_by(
                    'type', 'organization__name'))),
        name='purchasing-links',
        kwargs={'type_list': dict(models.PurchasingLink.LINK_TYPES),
                'member_only': True}),

    url(r'^campus-universal-transit-passes',
        ResourceItemListView.as_view(
            model=models.TransitPass,
            queryset=models.TransitPass.objects.order_by(
                    '-type', 'organization__country',
                    'organization__name')),
        name='transit-passes',
        kwargs={'type_list': dict(models.TransitPass.PASS_TYPES)}),

    green_building_url(
        url_string=r'^athletic-recreation-centers-stadiums',
        building_type='Green Athletic Buildings',
        image_url='http://www.aashe.org/files/univ_of_arizona_rec_center_0.jpg',
        image_alt='Univ Arizona',
        image_caption='University of Arizona Recreation Center'),

    green_building_url(
        url_string=r'^green-student-centers',
        building_type='Green Student Centers',
        image_url='http://www.aashe.org/files/sju_mckeown_0.jpg',
        image_alt='SJU McKeown',
        image_caption='St. John\'s University McKeown Center'),

    green_building_url(
        url_string=r'^green-libraries-campus',
        building_type='Green Libraries on Campus',
        image_url='http://www.aashe.org/files/thompson_library_1.jpg',
        image_alt='OSU Thompson Library',
        image_caption='Ohio State University Thompson Library',
        buildings_name='libraries'),

    green_building_url(
        url_string=r'^green-residence-halls',
        building_type='Green Residence Halls',
        image_url='http://www.aashe.org/files/ashdown_house_mit.jpg',
        image_alt='MIT Ashdown House',
        image_caption='MIT Ashdown House',
        # Model is empty, dunno why (mt)
        model=models.GreenResidenceHall
        ),

    green_building_url(
        url_string=r'^green-science-buildings',
        building_type='Green Science Buildings',
        image_url='http://www.aashe.org/files/brandeis.jpg',
        image_alt='Brandeis University Shapiro Science Center',
        image_caption='Brandeis University Shapiro Science Center'),

    )
