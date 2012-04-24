from django.conf.urls.defaults import patterns, url
from django.template.defaultfilters import slugify

from rc.resources.views import ResourceItemListView
from rc.resources.apps.operations import models

def url_name(surname):
    return 'resources:operations:' + surname

def green_building_url(url_string, building_type, image_url=None,
                       image_alt=None, image_caption=None,
                       buildings_name=None):
    if not buildings_name:
        buildings_name = ' '.join(building_type.split()[1:]).lower()
    return url(url_string,
               ResourceItemListView.as_view(
                   model=models.CampusGreenBuilding,
                   queryset=models.CampusGreenBuilding.objects.filter(
                           type__type=building_type).order_by(
                               'type', 'certification', 'organization__name'),
                   template_name='operations/campusgreenbuilding_list.html'),
               name=url_name('green-buildings:' +
                             slugify(building_type).replace('green-', '')),
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

    url(r'^resources/campus-alternative-transportation-websites',
        ResourceItemListView.as_view(
            model=models.TransportationWebsite,
            queryset=models.TransportationWebsite.objects.order_by(
                    'organization__name')),
        name=url_name('transportation-websites'),
        kwargs={'member_only': True}),

    url(r'^resources/bottled-water-elimination-and-reduction',
        ResourceItemListView.as_view(
            model=models.BottledWaterBan,
            queryset=models.BottledWaterBan.objects.order_by(
                    'type', 'organization__name')),
        name=url_name('bottled-water-bans'),
        kwargs={'ban_types': dict(models.BottledWaterBan.BAN_TYPES),
                'member_only': True}),

    url(r'^resources/campus-building-energy-dashboards',
        ResourceItemListView.as_view(
            model=models.BuildingDashboard,
            queryset=models.BuildingDashboard.objects.order_by(
                    'partner__name', 'organization__name')),
        name=url_name('building-dashboards'),
        kwargs={'title': 'Campus Building Energy Dashboards',
                'member_only': True}),

    url(r'^resources/biodiesel-campus-fleets',
        ResourceItemListView.as_view(
            model=models.BiodieselFleet,
            queryset=models.BiodieselFleet.objects.order_by(
                    'production', 'organization__country',
                    'organization__name')),
        name=url_name('biodiesel-fleets'),
        kwargs={'member_only': True,
                'production_types':
                dict(models.BiodieselFleet.PRODUCTION_TYPE)}),

    url(r'^resources/campus-bicycle-plans',
        ResourceItemListView.as_view(
            model=models.BicyclePlan,
            queryset=models.BicyclePlan.objects.order_by(
                    'organization__name')),
        name=url_name('bicycle-plans'),
        kwargs={'member_only': True}),

    url(r'^resources/campus-car-bans',
        ResourceItemListView.as_view(
            model=models.CarBan,
            queryset=models.CarBan.objects.order_by(
                    'type', 'organization__name')),
        name=url_name('car-bans'),
        kwargs={'ban_types': dict(models.CarBan.BAN_TYPES)}),

    url(r'^resources/campus-commuter-surveys',
        ResourceItemListView.as_view(
            model=models.CommuterSurvey,
            queryset=models.CommuterSurvey.objects.order_by(
                    'type', 'organization__name')),
        name=url_name('commuter-surveys'),
        kwargs={'survey_types': dict(models.CommuterSurvey.SURVEY_TYPES),
                'member_only': True}),

    url(r'^resources/campus-electric-vehicle-fleets',
        ResourceItemListView.as_view(
            model=models.ElectricFleet,
            queryset=models.ElectricFleet.objects.order_by(
                    'organization__country', 'organization__name')),
        name=url_name('electric-fleets'),
        kwargs={'member_only': True}),

    url(r'^resources/campus-energy-plans',
        ResourceItemListView.as_view(
            model=models.EnergyPlan,
            queryset=models.EnergyPlan.objects.order_by(
                    'organization__name')),
        name=url_name('energy-plans'),
        kwargs={'member_only': True}),

    url(r'^resources/campus-global-warming-commitments',
        ResourceItemListView.as_view(
            model=models.GlobalWarmingCommitment,
            queryset=models.GlobalWarmingCommitment.objects.order_by(
                    'organization__name')),
            name=url_name('global-warming-commitments')),

    url(r'^resources/campus-hybrid-vehicle-fleets',
        ResourceItemListView.as_view(
            model=models.HybridFleet,
            queryset=models.HybridFleet.objects.order_by(
                    'organization__country', 'organization__name')),
        name=url_name('hybrid-fleets'),
        kwargs={'member_only': True}),

    url(r'^resources/campus-recycling-and-waste-minimization-websites',
        ResourceItemListView.as_view(
            model=models.RecyclingWebsite,
            queryset=models.RecyclingWebsite.objects.order_by(
                    'organization__name')),
        name=url_name('recycling-websites'),
        kwargs={'member_only': True}),

    url(r'^resources/campus-water-conservation-efforts',
        ResourceItemListView.as_view(
            model=models.WaterConservationEffort,
            queryset=models.WaterConservationEffort.objects.order_by(
                    'organization__country', 'organization__name')),
        name=url_name('water-conservation-efforts'),
        kwargs={'member_only': True}),

    url(r'^resources/wind-power-campus-1',
        ResourceItemListView.as_view(
            model=models.WindTurbine,
            queryset=models.WindTurbine.objects.order_by(
                    'organization__country', 'organization__name')),
        name=url_name('wind-turbines'),
        kwargs={'member_only': True}),

    url(r'^resources/carsharing-campus',
        ResourceItemListView.as_view(
            model=models.CarShare,
            queryset=models.CarShare.objects.order_by(
                    'partner__name', 'organization__name')),
        name=url_name('car-shares'),
        kwargs={'member_only': True}),

    url(r'^resources/renewable-energy-research-centers',
        ResourceItemListView.as_view(
            model=models.RenewableResearchCenter,
            queryset=models.RenewableResearchCenter.objects.order_by(
                    'organization__name')),
        name=url_name('renewable-research-centers'),
        kwargs={'member_only': True}),

    url(r'^resources/campus-installations-stationary-fuel-cells',
        ResourceItemListView.as_view(
            model=models.FuelCell,
            queryset=models.FuelCell.objects.order_by('-size',
                                                      'organization__name')),
            name=url_name('fuel-cells')),

    url(r'^resources/sustainable-dining-initiatives-campus',
        ResourceItemListView.as_view(
            model=models.DiningInitiative,
            queryset=models.DiningInitiative.objects.order_by(
                    'ownership', 'organization__name')),
        name=url_name('dining-initiatives'),
        kwargs={'owners': dict(models.DiningInitiative.OWNERS),
                'member_only': True}),

    url(r'^resources/sustainable-landscaping-campus',
        ResourceItemListView.as_view(
            model=models.SustainableLandscape,
            queryset=models.SustainableLandscape.objects.order_by(
                    'organization__name')),
        name=url_name('sustainable-landscapes')),

    url(r'^resources/links-related-sustainable-purchasing-campus',
        ResourceItemListView.as_view(
            model=models.PurchasingLink,
            queryset=models.PurchasingLink.objects.order_by(
                    'type', 'organization__name')),
        name=url_name('purchasing-links'),
        kwargs={'type_list': dict(models.PurchasingLink.LINK_TYPES),
                'member_only': True}),

    url(r'^resources/campus-universal-transit-passes',
        ResourceItemListView.as_view(
            model=models.TransitPass,
            queryset=models.TransitPass.objects.order_by(
                    '-type', 'organization__country',
                    'organization__name')),
        name=url_name('transit-passes'),
        kwargs={'type_list': dict(models.TransitPass.PASS_TYPES)}),

    url(r'^resources/websites-campus-green-building',
        ResourceItemListView.as_view(
            model=models.GreenBuildingWebsite,
            queryset=models.GreenBuildingWebsite.objects.order_by('title')),
        name=url_name('green-building-websites')),

    green_building_url(
        url_string=r'^resources/athletic-recreation-centers-stadiums',
        building_type='Green Athletic Buildings',
        image_url='http://www.aashe.org/files/univ_of_arizona_rec_center_0.jpg',
        image_alt='Univ Arizona',
        image_caption='University of Arizona Recreation Center'),

    green_building_url(
        url_string=r'^resources/green-student-centers',
        building_type='Green Student Centers',
        image_url='http://www.aashe.org/files/sju_mckeown_0.jpg',
        image_alt='SJU McKeown',
        image_caption='St. John\'s University McKeown Center'),

    green_building_url(
        url_string=r'^resources/green-libraries-campus',
        building_type='Green Libraries on Campus',
        image_url='http://www.aashe.org/files/thompson_library_1.jpg',
        image_alt='OSU Thompson Library',
        image_caption='Ohio State University Thompson Library',
        buildings_name='libraries'),

    green_building_url(
        url_string=r'^resources/green-residence-halls',
        building_type='Green Residence Halls',
        image_url='http://www.aashe.org/files/ashdown_house_mit.jpg',
        image_alt='MIT Ashdown House',
        image_caption='MIT Ashdown House'),

    green_building_url(
        url_string=r'^resources/green-science-buildings',
        building_type='Green Science Buildings',
        image_url='http://www.aashe.org/files/brandeis.jpg',
        image_alt='Brandeis University Shapiro Science Center',
        image_caption='Brandeis University Shapiro Science Center'),

    )
