from django.conf.urls.defaults import patterns, url
from django.template.defaultfilters import slugify

from rc.resources.views import ResourceItemListView, \
     handle_missing_organizations
from rc.resources.apps.education import models


def url_name(surname):
    return 'resources:education:' + surname

def academic_centers_url_name(center_type_code):
    academic_center_types = dict(models.AcademicCenterType.CENTER_TYPES)
    return url_name('academic-centers:' +
                    slugify(academic_center_types[center_type_code]))

urlpatterns = patterns('',
    url(r'^resources/alumni-sustainability-networks$',
        ResourceItemListView.as_view(
            model=models.SustainabilityNetwork,
            queryset=handle_missing_organizations(
                models.SustainabilityNetwork.objects.all())),
        name=url_name('sustainability-networks')),


    url(r'^resources/campus-and-campus-community-gardens$',
        ResourceItemListView.as_view(
            model=models.CommunityGarden,
            queryset=handle_missing_organizations(
                models.CommunityGarden.objects.order_by(
                'organization__country', 'organization__name'))),
        name=url_name('community-gardens'),
        kwargs={'member_only': True}),

    url(r'^resources/campus-supported-agriculture-and-farms$',
        ResourceItemListView.as_view(
            model=models.CampusAgriculture,
            queryset=handle_missing_organizations(
                models.CampusAgriculture.objects.order_by(
                 'organization__country', 'organization__name'))),
        name=url_name('campus-agricultures'),
        kwargs={'member_only': True}),

    url(r'^resources/campus-sustainable-living-guides$',
        ResourceItemListView.as_view(
            model=models.LivingGuide,
            queryset=handle_missing_organizations(
                models.LivingGuide.objects.order_by(
                 'organization__country', 'organization__name'))),
        name=url_name('living-guides'),
        kwargs={'member_only': True}),

    url(r'^resources/campus-sustainability-mapstours$',
        ResourceItemListView.as_view(
            model=models.SustainabilityMap,
            queryset=handle_missing_organizations(
                models.SustainabilityMap.objects.order_by(
                 'organization__name'))),
            name=url_name('sustainability-maps')),

    url(r'^resources/surveys-sustainability-awareness-attitudes-and-values$',
        ResourceItemListView.as_view(
            model=models.SurveyOfAwareness,
            queryset=handle_missing_organizations(
                models.SurveyOfAwareness.objects.order_by(
                 'organization__name'))),
        name=url_name('surveys-of-awareness'),
        kwargs={'member_only': True}),

    url(r'^resources/sustainability-course-inventories$',
        ResourceItemListView.as_view(
            model=models.SustainabilityCourseInventory,
            queryset=handle_missing_organizations(
                models.SustainabilityCourseInventory.objects.order_by(
                'organization__name'))),
        name=url_name('sustainability-course-inventories'),
        kwargs={'member_only': True}),

    url(r'^resources/sustainability-faculty-development-workshops$',
        ResourceItemListView.as_view(
            model=models.FacultyWorkshop,
            queryset=handle_missing_organizations(
                models.FacultyWorkshop.objects.order_by(
                 'organization__name'))),
        name=url_name('faculty-workshops'),
        kwargs={'member_only': True}),

    url(r'^resources/sustainability-research-inventories$',
        ResourceItemListView.as_view(
            model=models.ResearchInventory,
            queryset=handle_missing_organizations(
                models.ResearchInventory.objects.order_by(
                 'organization__name'))),
        name=url_name('research-inventories'),
        kwargs={'member_only': True}),

    url(r'^resources/sustainability-related-syllabi-databases$',
        ResourceItemListView.as_view(
            model=models.SustainabilitySyllabus,
            queryset=handle_missing_organizations(
                models.SustainabilitySyllabus.objects.order_by(
                    'organization__name'))),
        name=url_name('sustainability-syllabi'),
        kwargs={'title':'Sustainability-Related Syllabi Databases',
                'member_only': True}),

    url('^resources/academic-centers-and-research-initiatives-sustainable-'
        'agriculture$',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=handle_missing_organizations(
                models.AcademicCenter.objects.filter(
                    type__type='AG').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'agriculture_list.html'),
        name=academic_centers_url_name('AG')),

    url('^resources/sustainable-design-academic-centers',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=handle_missing_organizations(
                models.AcademicCenter.objects.filter(
                    type__type='AR').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'architecture_list.html'),
        name=academic_centers_url_name('AR')),

    url('^resources/business-school-academic-centers-and-'
        'research-initiatives-sustainability',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=handle_missing_organizations(
                models.AcademicCenter.objects.filter(
                    type__type='BS').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'business_list.html'),
            name=academic_centers_url_name('BS')),

    url('^resources/research-centers-sustainable-development',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=handle_missing_organizations(
                models.AcademicCenter.objects.filter(
                    type__type='DS').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'developmentstudies_list.html'),
        name=academic_centers_url_name('DS')),

    url('^resources/academic-centers-ecological-economics',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=handle_missing_organizations(
                models.AcademicCenter.objects.filter(
                    type__type='EC').order_by('organization__country',
                                              'organization__name')),
            template_name='education/academiccenters/'
                          'economics_list.html'),
        name=academic_centers_url_name('EC')),

    url('^resources/'
        'academic-centers-sustainability-and-environmental-education',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=handle_missing_organizations(
                models.AcademicCenter.objects.filter(
                    type__type='ED').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'education_list.html'),
        name=academic_centers_url_name('ED')),

    url('^resources/sustainable-engineering-academic-centers',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=handle_missing_organizations(
                models.AcademicCenter.objects.filter(
                    type__type='EN').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'engineering_list.html'),
        name=academic_centers_url_name('EN')),

    url('^resources/academic-centers-focused-environmental-law',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=handle_missing_organizations(
                models.AcademicCenter.objects.filter(
                    type__type='LW').order_by('organization__country',
                                              'organization__name')),
            template_name='education/academiccenters/law_list.html'),
        name=academic_centers_url_name('LW')),

    url('^resources/academic-centers-and-research-inititatives-urban-studies',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=handle_missing_organizations(
                models.AcademicCenter.objects.filter(
                    type__type='US').order_by('organization__name')),
            template_name='education/academiccenters/'
                          'urbanstudies_list.html'),
        name=academic_centers_url_name('US')),

    url('^resources/courses-campus-sustainability',
        ResourceItemListView.as_view(
            model=models.CampusSustainabilityCourse,
            queryset=handle_missing_organizations(
                models.CampusSustainabilityCourse.objects.order_by(
                    'organization__name', 'title')),
            template_name='education/academiccenters/'
                          'campussustainabilitycourse_list.html'),
        name=url_name('campus-sustainability-courses')),

    )
