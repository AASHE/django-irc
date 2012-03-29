from django.conf.urls.defaults import patterns, include, url

from rc.resources.views import ResourceItemListView
import rc.resources.apps.education.models as edmodels


HIDE_RESOURCES_WITH_NO_ORGANIZATION = False


def handle_missing_organizations(qs):
    if HIDE_RESOURCES_WITH_NO_ORGANIZATION:
        qs = qs.exclude(organization=None)
    return qs

urlpatterns = patterns('',

    url(r'^resources/alumni-sustainability-networks$',
        ResourceItemListView.as_view(
            model=edmodels.SustainabilityNetwork,
            queryset=handle_missing_organizations(
                edmodels.SustainabilityNetwork.objects.all())),
        {'member_only': True}),

    url(r'^resources/campus-and-campus-community-gardens$', 
        ResourceItemListView.as_view(
            model=edmodels.CommunityGarden,
            queryset=handle_missing_organizations(
                edmodels.CommunityGarden.objects.order_by(
                'organization__country', 'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-supported-agriculture-and-farms$',
        ResourceItemListView.as_view(
            model=edmodels.CampusAgriculture,
            queryset=handle_missing_organizations(
                edmodels.CampusAgriculture.objects.order_by(
                 'organization__country', 'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-sustainable-living-guides$',
        ResourceItemListView.as_view(
            model=edmodels.LivingGuide,
            queryset=handle_missing_organizations(
                edmodels.LivingGuide.objects.order_by(
                 'organization__country', 'organization__name'))),
        {'member_only': True}),
        
    url(r'^resources/campus-sustainability-mapstours$',
        ResourceItemListView.as_view(
            model=edmodels.SustainabilityMap,
            queryset=handle_missing_organizations(
                edmodels.SustainabilityMap.objects.order_by(
                 'organization__name')))),

    url(r'^resources/surveys-sustainability-awareness-attitudes-and-values$',
        ResourceItemListView.as_view(
            model=edmodels.SurveyOfAwareness,
            queryset=handle_missing_organizations(
                edmodels.SurveyOfAwareness.objects.order_by(
                 'organization__name'))),
        {'member_only': True}),

    url(r'^resources/sustainability-course-inventories$',
        ResourceItemListView.as_view(
            model=edmodels.SustainabilityCourseInventory,
            queryset=handle_missing_organizations(
                edmodels.SustainabilityCourseInventory.objects.order_by(
                'organization__name'))),
        {'member_only': True}),

    url(r'^resources/sustainability-faculty-development-workshops$',
        ResourceItemListView.as_view(
            model=edmodels.FacultyWorkshop,
            queryset=handle_missing_organizations(
                edmodels.FacultyWorkshop.objects.order_by(
                 'organization__name'))),
        {'member_only': True}),

    url(r'^resources/sustainability-research-inventories$',
        ResourceItemListView.as_view(
            model=edmodels.ResearchInventory,
            queryset=handle_missing_organizations(
                edmodels.ResearchInventory.objects.order_by(
                 'organization__name'))),
        {'member_only': True}),

    url(r'^resources/sustainability-related-syllabi-databases$',
        ResourceItemListView.as_view(
            model=edmodels.SustainabilitySyllabus,
            queryset=handle_missing_organizations(
                edmodels.SustainabilitySyllabus.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),
        
    url('^resources/academic-centers-and-research-initiatives-sustainable-'
        'agriculture$',
        ResourceItemListView.as_view(
            model=edmodels.AcademicCenter,
            queryset=handle_missing_organizations(
                edmodels.AcademicCenter.objects.filter(
                    type__type='AG').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'agriculture_list.html')),
                          
    url('^resources/sustainable-design-academic-centers',
        ResourceItemListView.as_view(
            model=edmodels.AcademicCenter,
            queryset=handle_missing_organizations(
                edmodels.AcademicCenter.objects.filter(
                    type__type='AR').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'architecture_list.html')),

    url('^resources/business-school-academic-centers-and-'
        'research-initiatives-sustainability',
        ResourceItemListView.as_view(
            model=edmodels.AcademicCenter,
            queryset=handle_missing_organizations(
                edmodels.AcademicCenter.objects.filter(
                    type__type='BS').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'business_list.html')),

    url('^resources/research-centers-sustainable-development',
        ResourceItemListView.as_view(
            model=edmodels.AcademicCenter,
            queryset=handle_missing_organizations(
                edmodels.AcademicCenter.objects.filter(
                    type__type='DS').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'developmentstudies_list.html')),
                          
    url('^resources/academic-centers-ecological-economics',
        ResourceItemListView.as_view(
            model=edmodels.AcademicCenter,
            queryset=handle_missing_organizations(
                edmodels.AcademicCenter.objects.filter(
                    type__type='EC').order_by('organization__country',
                                              'organization__name')),
            template_name='education/academiccenters/'
                          'economics_list.html')),

    url('^resources/'
        'academic-centers-sustainability-and-environmental-education',
        ResourceItemListView.as_view(
            model=edmodels.AcademicCenter,
            queryset=handle_missing_organizations(
                edmodels.AcademicCenter.objects.filter(
                    type__type='ED').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'education_list.html')),

    url('^resources/sustainable-engineering-academic-centers',
        ResourceItemListView.as_view(
            model=edmodels.AcademicCenter,
            queryset=handle_missing_organizations(
                edmodels.AcademicCenter.objects.filter(
                    type__type='EN').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'engineering_list.html')),

    )

