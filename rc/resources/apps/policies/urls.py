from django.conf.urls.defaults import patterns, url

from rc.resources.views import ResourceItemListView, \
     handle_missing_organizations
from rc.resources.apps.policies import models


urlpatterns = patterns('',
    url(r'^resources/alumni-sustainability-funds',
        ResourceItemListView.as_view(
            model=models.AlumniFund,
            queryset=handle_missing_organizations(
                models.AlumniFund.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),
                       
    url(r'^resources/energy-efficient-appliance-procurement-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-living-wage-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-anti-idling-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/paper-procurement-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-stormwater-policies-plans',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/socially-responsible-investment-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/energy-conservation-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-sustainability-and-environmental-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-fair-trade-practices-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/telecommuting-alternative-work',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/water-conservation-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-sustainability-and-environmental-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/energy-efficient-appliance-procurement-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-living-wage-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-anti-idling-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/paper-procurement-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-stormwater-policies-plans',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/socially-responsible-investment-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/energy-conservation-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-sustainability-and-environmental-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-fair-trade-practices-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/telecommuting-alternative-work',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/water-conservation-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    url(r'^resources/campus-sustainability-and-environmental-policies',
        ResourceItemListView.as_view(
            model=models.ZZ,
            queryset=handle_missing_organizations(
                models.ZZ.objects.order_by(
                    'organization__name'))),
        {'member_only': True}),

    )

