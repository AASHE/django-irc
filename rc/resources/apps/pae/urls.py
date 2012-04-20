from django.conf.urls.defaults import patterns, url

from rc.resources.views import ResourceItemListView
from rc.resources.apps.pae import models


def url_name(surname):
    return 'resources:pae:' + surname

urlpatterns = patterns('',

    url(r'^resources/alumni-sustainability-funds',
        ResourceItemListView.as_view(
            model=models.AlumniFund,
            queryset=models.AlumniFund.objects.order_by('organization__name')),
        name=url_name('alumni-funds'),
        kwargs={'member_only': True}),

    url(r'^resources/master-plans-incorporate-sustainability',
        ResourceItemListView.as_view(
            model=models.MasterPlan,
            queryset=models.MasterPlan.objects.order_by(
                    'minor_reference_only', 'organization__name')),
        name=url_name('master-plans'),
        kwargs={'member_only': True}),

    url(r'^resources/campus-sustainability-assessment-tools',
        ResourceItemListView.as_view(
            model=models.AssessmentTool,
            queryset=models.AssessmentTool.objects.order_by(
                    'provider', 'organization__name')),
        name=url_name('assesment-tools'),
        kwargs={'member_only': True,
         'type_list': dict(models.AssessmentTool.CREATORS)}),

    url(r'^resources/campus-sustainability-blogs',
        ResourceItemListView.as_view(
            model=models.SustainabilityBlog,
            queryset=models.SustainabilityBlog.objects.order_by(
                    'type', 'title')),
        name=url_name('sustainability-blogs')),

    url(r'^resources/campus-sustainability-plans',
        ResourceItemListView.as_view(
            model=models.SustainabilityPlan,
            queryset=models.SustainabilityPlan.objects.order_by(
                    'organization__name')),
        name=url_name('sustainability-plans'),
        kwargs={'member_only': True}),

    url(r'^resources/campus-sustainability-revolving-loan-funds',
        ResourceItemListView.as_view(
            model=models.RevolvingLoanFund,
            queryset=models.RevolvingLoanFund.objects.order_by(
                    'organization__name', 'title')),
        name=url_name('revolving-loan-funds'),
        kwargs={'member_only': True}),

    )
