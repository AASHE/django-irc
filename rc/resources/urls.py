from django.conf.urls.defaults import patterns, include, url

import rc.resources.apps.education.views as edviews
import rc.resources.apps.education.models as edmodels

urlpatterns = patterns(
    'resources',
    url(r'^campus-and-campus-community-gardens$', 
        edviews.ResourceItemTablesByOrgCountryView.as_view(
            model=edmodels.CommunityGarden)),
    url(r'^campus-supported-agriculture-and-farms$',
        edviews.ResourceItemTablesByOrgCountryView.as_view(
            model=edmodels.CampusAgriculture),
        {'member_only': True}),
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
		 
