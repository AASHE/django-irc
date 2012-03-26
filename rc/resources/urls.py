from django.conf.urls.defaults import patterns, include, url

import rc.resources.apps.education.views as edviews

urlpatterns = patterns(
    'resources',
    url(r'campus-and-campus-community-gardens', 
        edviews.CommunityGardenListView.as_view()),
    url(r'campus-supported-agriculture-and-farms',
        edviews.CampusAgricultureListView.as_view()),
    )

"""
* http://www.aashe.org/resources
** http://www.aashe.org/resources/education-research-resources
***** http://www.aashe.org/resources/co-curricular-education-resources
******* http://www.aashe.org/resources/alumni-sustainability-networks
******* http://www.aashe.org/resources/
******* http://www.aashe.org/resources/campus-supported-agriculture-and-farms
***** http://www.aashe.org/resources/curriculum-resources
***** http://www.aashe.org/resources/resources-sustainability-research
"""		 
		 
