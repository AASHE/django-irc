from django.conf.urls.defaults import patterns, url

from rc.resources.views import ResourceItemListView
from rc.resources.apps.education import models


HIDE_RESOURCES_WITH_NO_ORGANIZATION = False


def handle_missing_organizations(qs):
    if HIDE_RESOURCES_WITH_NO_ORGANIZATION:
        qs = qs.exclude(organization=None)
    return qs

urlpatterns = patterns('',
    url(r'^resources/alumni-sustainability-networks$',
        ResourceItemListView.as_view(
            model=models.SustainabilityNetwork,
            queryset=handle_missing_organizations(
                models.SustainabilityNetwork.objects.all())),
        {'member_only': True}),

    url(r'^resources/campus-and-campus-community-gardens$', 
        ResourceItemListView.as_view(
            model=models.CommunityGarden,
            queryset=handle_missing_organizations(
                models.CommunityGarden.objects.order_by(
                'organization__country', 'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-supported-agriculture-and-farms$',
        ResourceItemListView.as_view(
            model=models.CampusAgriculture,
            queryset=handle_missing_organizations(
                models.CampusAgriculture.objects.order_by(
                 'organization__country', 'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-sustainable-living-guides$',
        ResourceItemListView.as_view(
            model=models.LivingGuide,
            queryset=handle_missing_organizations(
                models.LivingGuide.objects.order_by(
                 'organization__country', 'organization__name'))),
        {'member_only': True}),
        
    url(r'^resources/campus-sustainability-mapstours$',
        ResourceItemListView.as_view(
            model=models.SustainabilityMap,
            queryset=handle_missing_organizations(
                models.SustainabilityMap.objects.order_by(
                 'organization__name')))),

    url(r'^resources/surveys-sustainability-awareness-attitudes-and-values$',
        ResourceItemListView.as_view(
            model=models.SurveyOfAwareness,
            queryset=handle_missing_organizations(
                models.SurveyOfAwareness.objects.order_by(
                 'organization__name'))),
        {'member_only': True}),

    url(r'^resources/sustainability-course-inventories$',
        ResourceItemListView.as_view(
            model=models.SustainabilityCourseInventory,
            queryset=handle_missing_organizations(
                models.SustainabilityCourseInventory.objects.order_by(
                'organization__name'))),
        {'member_only': True}),

    url(r'^resources/sustainability-faculty-development-workshops$',
        ResourceItemListView.as_view(
            model=models.FacultyWorkshop,
            queryset=handle_missing_organizations(
                models.FacultyWorkshop.objects.order_by(
                 'organization__name'))),
        {'member_only': True}),

    url(r'^resources/sustainability-research-inventories$',
        ResourceItemListView.as_view(
            model=models.ResearchInventory,
            queryset=handle_missing_organizations(
                models.ResearchInventory.objects.order_by(
                 'organization__name'))),
        {'member_only': True}),

    url(r'^resources/sustainability-related-syllabi-databases$',
        ResourceItemListView.as_view(
            model=models.SustainabilitySyllabus,
            queryset=handle_missing_organizations(
                models.SustainabilitySyllabus.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),
        
    url('^resources/academic-centers-and-research-initiatives-sustainable-'
        'agriculture$',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=handle_missing_organizations(
                models.AcademicCenter.objects.filter(
                    type__type='AG').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'agriculture_list.html')),
                          
    url('^resources/sustainable-design-academic-centers',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=handle_missing_organizations(
                models.AcademicCenter.objects.filter(
                    type__type='AR').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'architecture_list.html')),

    url('^resources/business-school-academic-centers-and-'
        'research-initiatives-sustainability',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=handle_missing_organizations(
                models.AcademicCenter.objects.filter(
                    type__type='BS').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'business_list.html')),

    url('^resources/research-centers-sustainable-development',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=handle_missing_organizations(
                models.AcademicCenter.objects.filter(
                    type__type='DS').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'developmentstudies_list.html')),
                          
    url('^resources/academic-centers-ecological-economics',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=handle_missing_organizations(
                models.AcademicCenter.objects.filter(
                    type__type='EC').order_by('organization__country',
                                              'organization__name')),
            template_name='education/academiccenters/'
                          'economics_list.html')),

    url('^resources/'
        'academic-centers-sustainability-and-environmental-education',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=handle_missing_organizations(
                models.AcademicCenter.objects.filter(
                    type__type='ED').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'education_list.html')),

    url('^resources/sustainable-engineering-academic-centers',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=handle_missing_organizations(
                models.AcademicCenter.objects.filter(
                    type__type='EN').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'engineering_list.html')),

    url('^resources/academic-centers-focused-environmental-law',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=handle_missing_organizations(
                models.AcademicCenter.objects.filter(
                    type__type='LW').order_by('organization__country',
                                              'organization__name')),
            template_name='education/academiccenters/law_list.html')),

    url('^resources/academic-centers-and-research-inititatives-urban-studies',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=handle_missing_organizations(
                models.AcademicCenter.objects.filter(
                    type__type='US').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'urbanstudies_list.html')),

    url('^resources/courses-campus-sustainability',
        ResourceItemListView.as_view(
            model=models.CampusSustainabilityCourse,
            queryset=handle_missing_organizations(
                models.CampusSustainabilityCourse.objects.order_by(
                    'organization__name', 'title')),
            template_name='education/academiccenters/'
                          'campussustainabilitycourse_list.html')),

                          
    )

