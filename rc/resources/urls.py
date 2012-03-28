from django.conf.urls.defaults import patterns, include, url

from rc.resources.views import ResourceItemListView
import rc.resources.apps.education.models as edmodels

urlpatterns = patterns(
    'resources',
    url(r'^alumni-sustainability-networks$',
        ResourceItemListView.as_view(model=edmodels.SustainabilityNetwork),
        {'member_only': True}),
    url(r'^campus-and-campus-community-gardens$', 
        ResourceItemListView.as_view(model=edmodels.CommunityGarden),
        {'member_only': True,
         'order_by': ('organization__country', 'organization__name')}),
    url(r'^campus-supported-agriculture-and-farms$',
        ResourceItemListView.as_view(model=edmodels.CampusAgriculture),
        {'member_only': True,
         'order_by': ('organization__country', 'organization__name')}),
    url(r'^campus-sustainable-living-guides$',
        ResourceItemListView.as_view(model=edmodels.LivingGuide), 
        {'member_only': True,
         'order_by': ('organization__country', 'organization__name'),
         'exclude_resources_with_no_organization': True}),
    url(r'^campus-sustainability-mapstours$',
        ResourceItemListView.as_view(model=edmodels.SustainabilityMap),
        {'order_by': ('organization__name',)}),
    url(r'^surveys-sustainability-awareness-attitudes-and-values$',
        ResourceItemListView.as_view(model=edmodels.SurveyOfAwareness),
        {'member_only': True,
         'order_by': ('organization__name',)}),
    url(r'^sustainability-course-inventories$',
        ResourceItemListView.as_view(
            model=edmodels.SustainabilityCourseInventory),
        {'member_only': True,
         'order_by': ('organization__name',)}),
    url(r'^sustainability-faculty-development-workshops$',
        ResourceItemListView.as_view(model=edmodels.FacultyWorkshop),
        {'member_only': True,
         'order_by': ('organization__name',)}),
    url(r'^sustainability-research-inventories$',
        ResourceItemListView.as_view(model=edmodels.ResearchInventory),
        {'member_only': True,
         'order_by': ('organization__name',)}),            
    url(r'^sustainability-related-syllabi-databases$',
        ResourceItemListView.as_view(model=edmodels.SustainabilitySyllabus),
        {'member_only': True,
         'order_by': ('organization__name',),
         'exclude_resources_with_no_organization': True}),
    )

