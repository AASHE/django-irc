from django.conf.urls.defaults import patterns, url

from rc.resources.views import ResourceItemListView
from rc.resources.apps.pae import models
from rc.resources.apps.pae.views import StudentFeeListView

from aashe.aasheauth.decorators import members_only


urlpatterns = patterns('',

    url(r'^alumni-sustainability-funds',
        members_only(ResourceItemListView.as_view(
            model=models.AlumniFund,
            queryset=models.AlumniFund.objects.order_by('organization__name'))),
        name='alumni-funds',
        kwargs={'member_only': True}),

    url(r'^master-plans-incorporate-sustainability',
        members_only(ResourceItemListView.as_view(
            model=models.MasterPlan,
            queryset=models.MasterPlan.objects.order_by(
                    'minor_reference_only', 'organization__name'))),
        name='master-plans',
        kwargs={'member_only': True, 'title': 'Campus Master Plans that Incorporate Sustainability'}),

    url(r'^campus-sustainability-assessment-tools',
        members_only(ResourceItemListView.as_view(
            model=models.AssessmentTool,
            queryset=models.AssessmentTool.objects.order_by(
                    'provider', 'organization__name'))),
        name='assessment-tools',
        kwargs={'member_only': True,
         'type_list': dict(models.AssessmentTool.CREATORS)}),

    url(r'^campus-sustainability-blogs',
        ResourceItemListView.as_view(
            model=models.SustainabilityBlog,
            queryset=models.SustainabilityBlog.objects.order_by(
                    'type', 'title')),
        name='sustainability-blogs'),

    url(r'^campus-sustainability-plans',
        members_only(ResourceItemListView.as_view(
            model=models.SustainabilityPlan,
            queryset=models.SustainabilityPlan.objects.order_by(
                    'organization__name'))),
        name='sustainability-plans',
        kwargs={'member_only': True}),

    url(r'^campus-sustainability-revolving-loan-funds',
        members_only(ResourceItemListView.as_view(
            model=models.RevolvingLoanFund,
            queryset=models.RevolvingLoanFund.objects.order_by(
                    'organization__name', 'title'))),
        name='revolving-loan-funds',
<<<<<<< local
        kwargs={'member_only': True, 'title': 'Campus Sustainability Revolving Loan Fund'}),
=======
        kwargs={'title': 'Campus Sustainability Revolving Loan Funds',
                'member_only': True}),
>>>>>>> other

    url(r'^mandatory-student-fees-renewable-energy-and-energy-efficiency',
        StudentFeeListView.as_view(
            model=models.StudentFeesDescription,
            queryset=models.StudentFee.objects.order_by(
                    'organization__name')),
        name='student-fees',
        kwargs={'member_only': False, 'title': 'Dedicated Student Fees for Sustainability'}),

    )
