from django.conf.urls.defaults import patterns, url
from django.template.defaultfilters import slugify

from rc.resources.views import ResourceItemListView
from rc.resources.apps.education import models
from aashe.aasheauth.decorators import members_only


def academic_centers_url_name(center_type_code):
    academic_center_types = dict(models.AcademicCenterType.CENTER_TYPES)
    return 'academic-centers-' + slugify(academic_center_types[center_type_code])

urlpatterns = patterns(
    '',
    url(r'^alumni-sustainability-networks$',
        ResourceItemListView.as_view(
            model=models.SustainabilityNetwork,
            queryset=models.SustainabilityNetwork.objects.all()),
        name='sustainability-networks'),

    url(r'^campus-and-campus-community-gardens$',
        members_only(ResourceItemListView.as_view(
            model=models.CommunityGarden,
            queryset=models.CommunityGarden.objects.order_by(
                'organization__country', 'organization__name'))),
        name='community-gardens',
        kwargs={'title': 'Campus and Campus-Community Gardens',
                'member_only': True}),

    url(r'^campus-supported-agriculture-and-farms$',
        members_only(ResourceItemListView.as_view(
            model=models.CampusAgriculture,
            queryset=models.CampusAgriculture.objects.order_by(
                 'organization__country', 'organization__name'))),
        name='campus-agricultures',
        kwargs={'title': 'Campus Supported Agriculture and Farms',
                'member_only': True}),

    url(r'^campus-sustainable-living-guides$',
        members_only(ResourceItemListView.as_view(
            model=models.LivingGuide,
            queryset=models.LivingGuide.objects.order_by(
                 'organization__country', 'organization__name'))),
        name='living-guides',
        kwargs={'member_only': True}),

    url(r'^campus-sustainability-mapstours$',
        members_only(ResourceItemListView.as_view(
            model=models.SustainabilityMap,
            queryset=models.SustainabilityMap.objects.order_by(
                 'organization__country', 'organization__name'))),
            name='sustainability-maps',
            kwargs={'title': 'Campus Sustainability Maps and Tours'}),

    url(r'^surveys-sustainability-awareness-attitudes-and-values$',
        members_only(ResourceItemListView.as_view(
            model=models.SurveyOfAwareness,
            queryset=models.SurveyOfAwareness.objects.order_by(
                 'organization__name'))),
        name='surveys-of-awareness',
        kwargs={'member_only': True}),

    url(r'^sustainability-course-inventories$',
        members_only(ResourceItemListView.as_view(
            model=models.SustainabilityCourseInventory,
            queryset=models.SustainabilityCourseInventory.objects.order_by(
                'organization__name'))),
        name='sustainability-course-inventories',
        kwargs={'member_only': True}),

    url(r'^sustainability-faculty-development-workshops$',
        members_only(ResourceItemListView.as_view(
            model=models.FacultyWorkshop,
            queryset=models.FacultyWorkshop.objects.order_by(
                 'organization__name'))),
        name='faculty-workshops',
        kwargs={'member_only': True,
                'title': 'Campus-led Faculty Development Workshops on Sustainability'}),

    url(r'^sustainability-research-inventories$',
        members_only(ResourceItemListView.as_view(
            model=models.ResearchInventory,
            queryset=models.ResearchInventory.objects.order_by(
                 'organization__name'))),
        name='research-inventories',
        kwargs={'member_only': True}),

    url(r'^sustainability-related-syllabi-databases$',
        members_only(ResourceItemListView.as_view(
            model=models.SustainabilitySyllabus,
            queryset=models.SustainabilitySyllabus.objects.order_by(
                    'organization__name'))),
        name='sustainability-syllabi',
        kwargs={'title':'Sustainability-Related Syllabi Databases',
                'member_only': True}),

    url('^academic-centers-and-research-initiatives-sustainable-'
        'agriculture$',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=models.AcademicCenter.objects.filter(
                    type__type='AG').order_by('organization__name'),
            template_name='education/academiccenters/'
                          'agriculture_list.html'),
        name=academic_centers_url_name('AG')),

    url('^sustainable-design-academic-centers',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=models.AcademicCenter.objects.filter(
                    type__type='AR').order_by('organization__name'),
            template_name='education/academiccenters/'
                          'architecture_list.html'),
        name=academic_centers_url_name('AR')),

    url('^business-school-academic-centers-and-'
        'research-initiatives-sustainability',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=models.AcademicCenter.objects.filter(
                    type__type='BS').order_by('organization__name'),
            template_name='education/academiccenters/'
                          'business_list.html'),
            name=academic_centers_url_name('BS')),

    url('^research-centers-sustainable-development',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=models.AcademicCenter.objects.filter(
                    type__type='DS').order_by('organization__name'),
            template_name='education/academiccenters/'
                          'developmentstudies_list.html'),
        name=academic_centers_url_name('DS')),

   url('^academic-centers-ecological-economics',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=models.AcademicCenter.objects.filter(
                    type__type='EC').order_by('organization__country',
                                              'organization__name'),
            template_name='education/academiccenters/'
                          'economics_list.html'),
        name=academic_centers_url_name('EC')),

    url('^'
        'academic-centers-sustainability-and-environmental-education',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=models.AcademicCenter.objects.filter(
                    type__type='ED').order_by('organization__name'),
            template_name='education/academiccenters/'
                          'education_list.html'),
        name=academic_centers_url_name('ED')),

    url('^sustainable-engineering-academic-centers',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=models.AcademicCenter.objects.filter(
                    type__type='EN').order_by('organization__name'),
            template_name='education/academiccenters/'
                          'engineering_list.html'),
        name=academic_centers_url_name('EN')),

    url('^academic-centers-focused-environmental-law',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=models.AcademicCenter.objects.filter(
                    type__type='LW').order_by('organization__country',
                                              'organization__name'),
            template_name='education/academiccenters/law_list.html'),
        name=academic_centers_url_name('LW')),

    url('^academic-centers-and-research-inititatives-urban-studies',
        ResourceItemListView.as_view(
            model=models.AcademicCenter,
            queryset=models.AcademicCenter.objects.filter(
                    type__type='US').order_by('organization__name'),
            template_name='education/academiccenters/'
                          'urbanstudies_list.html'),
        name=academic_centers_url_name('US')),

    url('^courses-campus-sustainability',
        ResourceItemListView.as_view(
            model=models.CampusSustainabilityCourse,
            queryset=models.CampusSustainabilityCourse.objects.order_by(
                    'organization__name', 'title'),
            template_name='education/academiccenters/'
                          'campussustainabilitycourse_list.html'),
        name='campus-sustainability-courses'),

    )
