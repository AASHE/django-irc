from django.conf.urls.defaults import patterns, url

from rc.resources.views import ResourceItemListView
from rc.resources.apps.pae import models
from rc.resources.apps.pae.views import StudentFeeListView


urlpatterns = patterns('',

    url(r'^resources/alumni-sustainability-funds',
        ResourceItemListView.as_view(
            model=models.AlumniFund,
            queryset=models.AlumniFund.objects.order_by('organization__name')),
        name='alumni-funds',
        kwargs={'member_only': True}),

    url(r'^resources/master-plans-incorporate-sustainability',
        ResourceItemListView.as_view(
            model=models.MasterPlan,
            queryset=models.MasterPlan.objects.order_by(
                    'minor_reference_only', 'organization__name')),
        name='master-plans',
        kwargs={'member_only': True}),

    url(r'^resources/campus-sustainability-assessment-tools',
        ResourceItemListView.as_view(
            model=models.AssessmentTool,
            queryset=models.AssessmentTool.objects.order_by(
                    'provider', 'organization__name')),
        name='assessment-tools',
        kwargs={'member_only': True,
         'type_list': dict(models.AssessmentTool.CREATORS)}),

    url(r'^resources/campus-sustainability-blogs',
        ResourceItemListView.as_view(
            model=models.SustainabilityBlog,
            queryset=models.SustainabilityBlog.objects.order_by(
                    'type', 'title')),
        name='sustainability-blogs'),

    url(r'^resources/campus-sustainability-plans',
        ResourceItemListView.as_view(
            model=models.SustainabilityPlan,
            queryset=models.SustainabilityPlan.objects.order_by(
                    'organization__name')),
        name='sustainability-plans',
        kwargs={'member_only': True}),

    url(r'^resources/campus-sustainability-revolving-loan-funds',
        ResourceItemListView.as_view(
            model=models.RevolvingLoanFund,
            queryset=models.RevolvingLoanFund.objects.order_by(
                    'organization__name', 'title')),
        name='revolving-loan-funds',
        kwargs={'member_only': True}),

    url(r'^resources/mandatory-student-fees-renewable-energy-and-energy-efficiency',
        StudentFeeListView.as_view(
            model=models.StudentFeesDescription,
            queryset=models.StudentFee.objects.order_by(
                    'organization__name')),
        name='student-fees',
        kwargs={'member_only': False}),

    )
