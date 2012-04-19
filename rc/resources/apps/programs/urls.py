from django.conf.urls.defaults import patterns, url

from rc.resources.views import ResourceItemListView, \
     handle_missing_organizations
from rc.resources.apps.programs import models, views


def url_name(surname):
    return 'resources:programs:' + surname

urlpatterns = patterns('',

    url(r'^resources/bicycle-share-programs',
        ResourceItemListView.as_view(
            model=models.Program,
            queryset=handle_missing_organizations(
                models.Program.objects.filter(
                    type__type__in=['Free Bicycle Share Programs',
                                    'Bicycle Rental Programs']).order_by(
                    '-type__type', 'organization__country',
                    'organization__name')),
            template_name=('programs/program_table_by_type_by_country_'
                           'by_org_name_list.html')),
            name=url_name('bicycle-share-and-rental'),
            kwargs={'member_only': True}),

    url(r'^resources/campus-composting-programs',
        ResourceItemListView.as_view(
            model=models.Program,
            queryset=handle_missing_organizations(
                models.Program.objects.filter(
                    type__type='Campus Composting Program').order_by(
                    'organization__name')),
            template_name=('programs/program_table_by_org_name_list.html')),
            name=url_name('campus-composting'),
            kwargs={'member_only': True}),

    url(r'^resources/campus-surplus-recycling',
        ResourceItemListView.as_view(
            model=models.Program,
            queryset=handle_missing_organizations(
                models.Program.objects.filter(
                    type__type='Surplus Property Recycling').order_by(
                    'organization__country', 'organization__name')),
            template_name=('programs/campus_surplus_recycling_list.html')),
            name=url_name('surplus-property-recycling'),
            kwargs={'member_only': True}),

    url(r'^resources/green-cleaning',
        views.GreenCleaningProgramAndPolicyListView.as_view(
            model=models.Program,
            template_name=('programs/green_cleaning_programs_and_policies'
                           '_list.html')),
            name=url_name('green-cleaning'),
            kwargs={'member_only': True}),

    url(r'^resources/green-office-programs',
        ResourceItemListView.as_view(
            model=models.Program,
            queryset=handle_missing_organizations(
                models.Program.objects.filter(
                    type__type='Green Office').order_by(
                    'organization__country', 'organization__name')),
            template_name=('programs/green_office_list.html')),
            name=url_name('green-office'),
            kwargs={'member_only': True}),

    url(r'^resources/peer-peer-sustainability-outreach-campaigns',
        ResourceItemListView.as_view(
            model=models.Program,
            queryset=handle_missing_organizations(
                models.Program.objects.filter(
                    type__type='Student Sustainability Educator').order_by(
                    'organization__name')),
            template_name='programs/student_sustainability_educator_list.html'),
            name=url_name('student-sustainability-educator'),
            kwargs={'member_only': True}),

        )
