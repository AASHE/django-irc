from django.conf.urls.defaults import patterns, url

from rc.resources.views import ResourceItemListView, \
     handle_missing_organizations
from rc.resources.apps.programs import models, views


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
            {'member_only': True}),

    url(r'^resources/campus-composting-programs',
        ResourceItemListView.as_view(
            model=models.Program,
            queryset=handle_missing_organizations(
                models.Program.objects.filter(
                    type__type='Campus Composting Program').order_by(
                    'organization__name')),
            template_name=('programs/program_table_by_org_name_list.html')),
            {'member_only': True}),

    url(r'^resources/campus-surplus-recycling',
        ResourceItemListView.as_view(
            model=models.Program,
            queryset=handle_missing_organizations(
                models.Program.objects.filter(
                    type__type='Surplus Property Recycling').order_by(
                    'organization__country', 'organization__name')),
            template_name=('programs/campus_surplus_recycling_list.html')),
            {'member_only': True}),

    url(r'^resources/green-cleaning',
        views.GreenCleaningProgramAndPolicyListView.as_view(
                model=models.Program,
                template_name=('programs/green_cleaning_programs_and_policies'
                               '_list.html')),
                {'member_only': True}),

    url(r'^resources/green-office-programs',
        ResourceItemListView.as_view(
            model=models.Program,
            queryset=handle_missing_organizations(
                models.Program.objects.filter(
                    type__type='Green Office').order_by(
                    'organization__country', 'organization__name')),
            template_name=('programs/green_office_list.html')),
            {'member_only': True}),
    )
