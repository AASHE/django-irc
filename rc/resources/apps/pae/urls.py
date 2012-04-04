from django.conf.urls.defaults import patterns, url

from rc.resources.views import ResourceItemListView, \
     handle_missing_organizations
from rc.resources.apps.pae import models


urlpatterns = patterns('',

    url(r'^resources/alumni-sustainability-funds',
        ResourceItemListView.as_view(
            model=models.AlumniFund,
            queryset=handle_missing_organizations(
                models.AlumniFund.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/master-plans-incorporate-sustainability',
        ResourceItemListView.as_view(
            model=models.MasterPlan,
            queryset=handle_missing_organizations(
                models.MasterPlan.objects.order_by(
                    'minor_reference_only', 'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-sustainability-assessment-tools',
        ResourceItemListView.as_view(
            model=models.AssessmentTool,
            queryset=handle_missing_organizations(
                models.AssessmentTool.objects.order_by(
                    'provider', 'organization__name'))),
        {'member_only': True,
         'type_list': dict(models.AssessmentTool.CREATORS)}),

    url(r'^resources/campus-sustainability-blogs',
        ResourceItemListView.as_view(
            model=models.SustainabilityBlog,
            queryset=handle_missing_organizations(
                models.SustainabilityBlog.objects.order_by(
                    'type', 'title')))),

        
    )

