from django.conf.urls.defaults import patterns, url

from rc.resources.views import ResourceItemListView, \
     handle_missing_organizations
from rc.resources.apps.policies import models

def policy_url(url_string, resource_area):
    return url(url_string,
               ResourceItemListView.as_view(
                   model=models.Policy,
                   queryset=handle_missing_organizations(
                       models.Policy.objects.filter(
                           resource_area__area=resource_area).order_by(
                               'organization__name'))), 
               {'member_only': True,
                'resource_area': resource_area})

def policy_by_country_by_org_name_url(url_string, resource_area,
                                      page_title=None):
    template_name = 'policies/policy_by_country_by_org_name_list.html'

    if not page_title:
        page_title = resource_area
    
    return url(url_string,
               ResourceItemListView.as_view(
                    model=models.Policy,
                    queryset=handle_missing_organizations(
                        models.Policy.objects.filter(
                            resource_area__area=resource_area).order_by(
                                'organization__country',
                                'organization__name')),
                    template_name=template_name),
                    {'member_only': True,
                     'resource_area': resource_area,
                     'page_title': page_title})

urlpatterns = patterns('',

    policy_url(r'^resources/energy-efficient-appliance-procurement-policies',
               'Energy Efficient Appliance Procurement Policies'),

    policy_by_country_by_org_name_url(
        url_string=r'^resources/campus-stormwater-policies-plans',
        resource_area='Campus Stormwater Policy',
        page_title='Campus Stormwater Policies / Plans'),
        

               
    # url(r'^resources/campus-living-wage-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/campus-anti-idling-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/paper-procurement-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/campus-stormwater-policies-plans',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/socially-responsible-investment-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/energy-conservation-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/campus-sustainability-and-environmental-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/campus-fair-trade-practices-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/telecommuting-alternative-work',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/water-conservation-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/campus-sustainability-and-environmental-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/energy-efficient-appliance-procurement-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/campus-living-wage-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/campus-anti-idling-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/paper-procurement-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/campus-stormwater-policies-plans',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/socially-responsible-investment-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/energy-conservation-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/campus-sustainability-and-environmental-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/campus-fair-trade-practices-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/telecommuting-alternative-work',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/water-conservation-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    # url(r'^resources/campus-sustainability-and-environmental-policies',
    #     ResourceItemListView.as_view(
    #         model=models.ZZ,
    #         queryset=handle_missing_organizations(
    #             models.ZZ.objects.order_by(
    #                 'organization__name'))),
    #     {'member_only': True}),

    )

