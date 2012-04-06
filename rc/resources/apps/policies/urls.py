from django.conf.urls.defaults import patterns, url

from rc.resources.views import ResourceItemListView, \
     handle_missing_organizations
from rc.resources.apps.policies import models

def policy_url(url_string, resource_area, page_title=None, 
               with_description=False, table_list=False,
               template_name=None, opening_text=None,
               member_only=False):
    if not page_title:
        page_title = resource_area

    if not template_name:
        if not table_list:
            template_name = 'policies/policy_text_by_org_name_list.html'
        else:
            template_name = 'policies/policy_table_by_org_name_list.html'

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
                    'opening_text': opening_text,
                    'member_only': member_only })

def policy_by_country_by_org_name_url(url_string, resource_area,
                                      page_title=None, opening_text=None,
                                      member_only=False):
    template_name = 'policies/policy_table_by_country_by_org_name_list.html'

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
                     'opening_text': opening_text,
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
        page_title='Telecommuting (Alternative Work) Policies',
        member_only=True),

    policy_by_country_by_org_name_url(
        url_string=r'^resources/water-conservation-policies',
        resource_area='Water Conservation Policies', 
        member_only=True),

    policy_url(
        r'^resources/campus-living-wage-policies',
        resource_area='Campus Living Wage Policy',
        with_description=True,
        page_title='Campus Living Wage Policies', 
        member_only=True),

    policy_url(
        r'^resources/campus-anti-idling-policies',
        resource_area='Campus Anti-Idling Policies',
        with_description=True,
        member_only=True),

    policy_url(
        r'^resources/paper-procurement-policies',
        resource_area='Campus Paper Procurement Policies',
        page_title='Paper Procurement Policies',
        with_description=True,
        member_only=True),

    policy_url(
        r'^resources/integrated-pest-management-policies',
        resource_area='Integrated Pest Management Policy',
        page_title='Integrated Pest Management Policies',        
        table_list=True,
        member_only=True),

    policy_url(
        r'^resources/trademark-licensee-code-conduct',
        resource_area='Licensee Code of Conduct', 
        page_title='Trademark Licensee Code of Conduct', 
        table_list=True,
        member_only=True),

    policy_url(
        r'^resources/campus-recycling-and-waste-minimization-policies',
        resource_area='Recycling / Waste Minimization Policy',
        page_title='Campus Recycling and Waste Minimization Policies',
        table_list=True,
        opening_text="""This resource compiles campus waste management 
                        policies that focus on waste minimization and/or 
                        recycling.""",
        member_only=True),

    url(r'^resources/campus-fair-trade-practices-policies',
        ResourceItemListView.as_view(
            model=models.FairTradePolicy,
            queryset=handle_missing_organizations(
                models.FairTradePolicy.objects.order_by(
                    'organization__country', 'organization__name'))),
            {'member_only': True}),
        
    )

