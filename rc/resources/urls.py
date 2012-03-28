from django.conf.urls.defaults import patterns, include, url

from rc.resources.views import ResourceItemListView
import rc.resources.apps.education.models as edmodels

urlpatterns = patterns(
    '',
    url(r'^resources/alumni-sustainability-networks$',
        ResourceItemListView.as_view(model=edmodels.SustainabilityNetwork),
        {'member_only': True}),
    url(r'^resources/campus-and-campus-community-gardens$', 
        ResourceItemListView.as_view(model=edmodels.CommunityGarden),
        {'member_only': True,
         'order_by': ('organization__country', 'organization__name')}),
    url(r'^resources/campus-supported-agriculture-and-farms$',
        ResourceItemListView.as_view(model=edmodels.CampusAgriculture),
        {'member_only': True,
         'order_by': ('organization__country', 'organization__name')}),
    url(r'^resources/campus-sustainable-living-guides$',
        ResourceItemListView.as_view(model=edmodels.LivingGuide), 
        {'member_only': True,
         'order_by': ('organization__country', 'organization__name'),
         'exclude_resources_with_no_organization': True}),
    url(r'^resources/campus-sustainability-mapstours$',
        ResourceItemListView.as_view(model=edmodels.SustainabilityMap),
        {'order_by': ('organization__name',)}),
    url(r'^resources/surveys-sustainability-awareness-attitudes-and-values$',
        ResourceItemListView.as_view(model=edmodels.SurveyOfAwareness),
        {'member_only': True,
         'order_by': ('organization__name',)}),
    url(r'^resources/sustainability-course-inventories$',
        ResourceItemListView.as_view(
            model=edmodels.SustainabilityCourseInventory),
        {'member_only': True,
         'order_by': ('organization__name',)}),
    url(r'^resources/sustainability-faculty-development-workshops$',
        ResourceItemListView.as_view(model=edmodels.FacultyWorkshop),
        {'member_only': True,
         'order_by': ('organization__name',)}),
    url(r'^resources/sustainability-research-inventories$',
        ResourceItemListView.as_view(model=edmodels.ResearchInventory),
        {'member_only': True,
         'order_by': ('organization__name',)}),            
    url(r'^resources/sustainability-related-syllabi-databases$',
        ResourceItemListView.as_view(model=edmodels.SustainabilitySyllabus),
        {'member_only': True,
         'order_by': ('organization__name',),
         'exclude_resources_with_no_organization': True}),

    url('^resources/academic-centers-and-research-initiatives-sustainable-agriculture$',
        ResourceItemListView.as_view(model=edmodels.AcademicCenter),
        {'order_by': ('organization__name',),
         'filter': ('academiccentertype__type="AG"',),
         'template_name': 'academiccenteronsustainableagriculture_list.html'}),
         
    )

