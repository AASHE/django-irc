from django.conf.urls.defaults import patterns, include, url

from rc.resources.views import ResourceItemListView, \
     ResourceItemListByOrgNameView, ResourceItemListByOrgCountryView
import rc.resources.apps.education.models as edmodels

urlpatterns = patterns(
    '',
    url(r'^resources/alumni-sustainability-networks$',
        ResourceItemListView.as_view(model=edmodels.SustainabilityNetwork),
        {'member_only': True}),
    # # Campus Case Studies on Sustainability in Co-Curricular Education
    # url(r'resources/case-studies/keyword/79',
    #     None, {'member-only': True}),
    url(r'^resources/campus-and-campus-community-gardens$', 
        ResourceItemListByOrgCountryView.as_view(
            model=edmodels.CommunityGarden),
        {'member_only': True}),
    url(r'^resources/campus-supported-agriculture-and-farms$',
        ResourceItemListByOrgCountryView.as_view(
            model=edmodels.CampusAgriculture),
        {'member_only': True}),
    url(r'^resources/campus-sustainable-living-guides$',
        ResourceItemListByOrgCountryView.as_view(
            model=edmodels.LivingGuide), 
        {'member_only': True}),
    url(r'^resources/campus-sustainability-mapstours$',
        ResourceItemListByOrgNameView.as_view(
            model=edmodels.SustainabilityMap)),
    url(r'^resources/surveys-sustainability-awareness-attitudes-and-values$',
        ResourceItemListByOrgNameView.as_view(model=edmodels.SurveyOfAwareness),
        {'member_only': True}),
    url(r'^resources/sustainability-course-inventories$',
        ResourceItemListByOrgNameView.as_view(
            model=edmodels.SustainabilityCourseInventory),
        {'member_only': True}),
    url(r'^resources/sustainability-faculty-development-workshops$',
        ResourceItemListByOrgNameView.as_view(
            model=edmodels.FacultyWorkshop),
        {'member_only': True}),
    url(r'^resources/sustainability-research-inventories$',
        ResourceItemListByOrgNameView.as_view(
            model=edmodels.ResearchInventory),
        {'member_only': True}),            
    )

