from django.conf.urls.defaults import patterns, url

from rc.resources.views import ResourceItemListView, \
     handle_missing_organizations
from rc.resources.apps.policies import models

def policy_url(url_string, resource_area, page_title=None, 
               with_description=False, member_only=False):
    if not page_title:
        page_title = resource_area

    template_name = 'policies/policy_list.html'

    return url(url_string,
               ResourceItemListView.as_view(
                   model=models.Policy,
                   queryset=handle_missing_organizations(
                       models.Policy.objects.filter(
                           resource_area__area=resource_area).order_by(
                               'organization__name')),
                   template_name=template_name), 
                   {'resource_area': resource_area,
                    'page_title': page_title,
                    'with_description': with_description,
                    'member_only': member_only })

def policy_by_country_by_org_name_url(url_string, resource_area,
                                      page_title=None, member_only=False):
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
                    {'resource_area': resource_area,
                     'page_title': page_title,
                     'member_only': member_only })

def policy_by_category_by_org_name_url(url_string, resource_area,
                                      page_title=None, member_only=False):
    template_name = 'policies/policy_text_by_category_by_org_name_list.html'

    if not page_title:
        page_title = resource_area
    
    return url(url_string,
               ResourceItemListView.as_view(
                    model=models.Policy,
                    queryset=handle_missing_organizations(
                        models.Policy.objects.filter(
                            resource_area__area=resource_area).order_by(
                                'category', 'organization__name')),
                    template_name=template_name),
                    {'resource_area': resource_area,
                     'page_title': page_title,
                     'member_only': member_only })


urlpatterns = patterns('',

    policy_url(
        r'^resources/energy-efficient-appliance-procurement-policies',
        resource_area='Energy Efficient Appliance Procurement Policies',
        with_description=True,
        member_only=True),

    policy_by_country_by_org_name_url(
        url_string=r'^resources/campus-stormwater-policies-plans',
        resource_area='Campus Stormwater Policy',
        page_title='Campus Stormwater Policies / Plans',
        member_only=True),

    policy_url(url_string=r'^resources/energy-conservation-policies',
               resource_area='Energy Conservation Policy', 
               page_title='Campus Sustainable Energy Policies'),

    policy_url(
        r'^resources/campus-sustainable-procurement-policies',
        resource_area='General / Comprehensive Procurement Policy',
        with_description=True,
        page_title='Campus Sustainable Procurement Policies',
        member_only=True),

    policy_by_category_by_org_name_url(
        r'^resources/campus-sustainability-and-environmental-policies',
        resource_area='General Sustainability Policy',
        page_title='Campus Sustainability and Environmental Policies',
        member_only=True),

    policy_by_country_by_org_name_url(
        url_string=r'^resources/telecommuting-alternative-work',
        resource_area='Telecommuting and Alternative Work Policies',
        page_title='Campus Stormwater Policies / Plans',
        member_only=True),

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

