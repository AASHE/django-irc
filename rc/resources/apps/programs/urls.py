from django.conf.urls.defaults import patterns, url

from rc.resources.views import ResourceItemListView
from rc.resources.apps.programs import models, views


urlpatterns = patterns('',

    url(r'^bicycle-share-programs$',
        ResourceItemListView.as_view(
            model=models.Program,
            queryset=models.Program.objects.published().filter(
                    type__type__in=['Free Bicycle Share Programs',
                                    'Bicycle Rental Programs']).order_by(
                    '-type__type', 'organization__country',
                    'organization__name'),
            template_name='programs/bicycle_share_list.html'),
        name='bicycle-share-and-rental',
        kwargs={'member_only': True,
                'title': 'Bicycle Sharing & Rental Programs'}),

    url(r'^campus-composting-programs$',
        ResourceItemListView.as_view(
            model=models.Program,
            queryset=models.Program.objects.published().filter(
                    type__type='Campus Composting Program').order_by(
                    'organization__name'),
            template_name='programs/campus_composting_list.html'),
        name='campus-composting',
        kwargs={'member_only': True, 'title': 'Campus Composting Programs'}),

    url(r'^campus-surplus-recycling$',
        ResourceItemListView.as_view(
            model=models.Program,
            queryset=models.Program.objects.published().filter(
                    type__type='Surplus Property Recycling').order_by(
                    'organization__country', 'organization__name'),
            template_name=('programs/campus_surplus_recycling_list.html')),
        name='surplus-property-recycling',
        kwargs={'member_only': True, 'title': 'Campus Surplus Property Recycling Programs'}),

    url(r'^e-waste-programs-policies-and-events$',
        views.ElectronicWasteProgramPolicyAndEventListView.as_view(
            model=models.Program,
            template_name=('programs/electronic_waste_program_policy_'
                           'and_event_list.html')),
        name='electronic-waste',
        kwargs={'member_only': True, 'title': 'Campus Electronic Waste Programs, Policies, and Events'}),

    url(r'^green-cleaning$',
        views.GreenCleaningProgramAndPolicyListView.as_view(
            model=models.Program,
            template_name=('programs/green_cleaning_program_and_policy'
                           '_list.html')),
        name='green-cleaning',
        kwargs={'member_only': True, 'title': 'Campus Green Cleaning Programs and Policies'}),

    url(r'^green-office-programs$',
        ResourceItemListView.as_view(
            model=models.Program,
            queryset=models.Program.objects.published().filter(
                    type__type='Green Office').order_by(
                    'organization__country', 'organization__name'),
            template_name=('programs/green_office_list.html')),
        name='green-office',
        kwargs={'member_only': True, 'title': 'Campus Green Office Programs'}),

    url(r'^peer-peer-sustainability-outreach-campaigns$',
        ResourceItemListView.as_view(
            model=models.Program,
            queryset=models.Program.objects.published().filter(
                    type__type='Student Sustainability Educator').order_by(
                    'organization__name'),
            template_name='programs/student_sustainability_educator_list.html'),
        name='student-sustainability-educator',
        kwargs={'title': 'Student Peer-to-Peer Sustainability Education Programs'}),
        )
