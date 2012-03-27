from django.conf.urls.defaults import patterns, include, url

from rc.resources.views import ResourceItemListView
import rc.resources.apps.education.views as edviews
import rc.resources.apps.education.models as edmodels

urlpatterns = patterns(
    '',
    url(r'^resources/campus-and-campus-community-gardens$', 
        edviews.ResourceItemTablesByOrgCountryView.as_view(
            model=edmodels.CommunityGarden),
        {'member_only': True}),
    url(r'^resources/campus-supported-agriculture-and-farms$',
        edviews.ResourceItemTablesByOrgCountryView.as_view(
            model=edmodels.CampusAgriculture),
        {'member_only': True}),
    # Alumni Sustainability Networks
    #    url(r'^resources/alumni-sustainability-networks$',    
    url(r'^resources/alumni-sustainability-networks$',
        ResourceItemListView.as_view(model=edmodels.SustainabilityNetwork),
        {'member_only': True}),
    # # Campus Case Studies on Sustainability in Co-Curricular Education
    # url(r'resources/case-studies/keyword/79',
    #     None, {'member-only': True}),
    # # Campus and Campus-Community Gardens
    # url(r'resources/campus-community-gardens',
    #     None, {'member_only': True}),
    # # Campus Supported Agriculture and Farms
    # url(r'resources/campus-supported-agriculture-and-farms',
    #     None, {'member_only': True}),
    # # Campus Sustainability Living Guides
    # url(r'resources/campus-sustainable-living-guides',
    #     None, {'member_only': True}),
    # # Dorm vs Dorm Sustainability Competitions
    # url(r'http://www.youtube.com/aasheorg#g/c/7606C262CE970EE4',
    #     None),
    # # Outreach Materials for Campus Sustainability
    # url(r'resources/outreach.php',
    #     None),
    # # Student Sustainability Educator Programs
    # url(r'resources/peer2peer.php',
    #     None),
    # # Student Sustainability Leadership Stories
    # url(r'resources/student_leadership_essays.php',
    #     None, {'member_only': True}
    # # AASHE Bulletin Articles on Sustainability in Co-Curricular Education
    # url(r'resources/bulletin/keyword/257',
    #     None, {'member_only': True}),
    # # AASHE Blog Posts on Sustainability in Co-Curricular Education        
    # url(r'category/blog-topics/campus-culture',
    #     None),
    # # Student Research on Sustainability in Co-Curricular Education  
    # url(r'resources/student-research/keyword/79', 
    #     None, {'member_only': True}),
    # # AASHE Discussion Forum on Sustainability in Co-Curricular Education  
    # url(r'forums/co-curricular-education',
    #     None),

    # # Engaging Students in STARS: A Student and Staff Perspective (Apr. 2010)  
    # url(r'https://stars.aashe.org/pages/news-events/stars-webinars/'
    #     '2010-stars-webinars.html#apr2010', None),

    # # Presentations from AASHE Conferences (2010- ) Related to
    # # Sustainability in Co-Curricular Education
    # url(r'resources/conference/search?keys=&amp%3B'
    #     r'field_stars_category_value[0]=290&amp%3B'
    #     r'field_session_materials_list=All', 
    #     None)
    )

