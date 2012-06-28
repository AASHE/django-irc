from django.conf.urls.defaults import patterns, url
from django.template.defaultfilters import slugify

from rc.resources.views import ResourceItemListView
from rc.resources.apps.policies import models

from aashe.aasheauth.decorators import members_only


def policy_url(url_string, policy_type, page_title='',
               with_description=False, table_list=False,
               template_name=None, opening_text='', bold_org_name=True,
               member_only=False):
    '''Returns a url for policies.Policy, filtered by pollicy_type,
    and sorted by organization__name.  If table_list is True, a
    template describing a table of Policies is used; else, a template
    describing a list of Policies is used.'''

    if not page_title:
        page_title = policy_type + ' policies'

    if not template_name:
        if not table_list:
            template_name = 'policies/policy_text_by_org_name_list.html'
        else:
            template_name = 'policies/policy_table_by_org_name_list.html'

    view = ResourceItemListView.as_view(
        model=models.Policy,
        queryset=models.Policy.objects.filter(
            type__type=policy_type).order_by('organization__name'),
        template_name=template_name)
    if member_only:
        view = members_only(view)

    return url(url_string, view,
                name=slugify(policy_type),
                kwargs={'page_title': page_title,
                        'title': page_title,
                        'with_description': with_description,
                        'opening_text': opening_text,
                        'bold_org_name': bold_org_name,
                        'member_only': member_only })

def policy_by_country_by_org_name_url(url_string, policy_type,
                                      page_title='', opening_text='',
                                      member_only=False):
    '''Returns a url for policies.Policy, filtered by policy_type,
    and sorted by organization__country and then organization__name. A
    template describing a table of Policies is used.'''

    template_name = 'policies/policy_table_by_country_by_org_name_list.html'

    if not page_title:
        page_title = policy_type + ' policies'

    view = ResourceItemListView.as_view(
        model=models.Policy,
        queryset=models.Policy.objects.filter(
            type__type=policy_type).order_by(
            'organization__country', 'organization__name'),
        template_name=template_name)
    if member_only:
        view = members_only(view)

    return url(url_string, view,
                name=slugify(policy_type),
                kwargs={'page_title': page_title,
                        'opening_text': opening_text,
                        'member_only': member_only })

def policy_by_category_by_org_name_url(url_string, policy_type,
                                       page_title='', member_only=False):
    '''Returns a url for policies.Policy, filtered by policy_type,
    and sorted by category and then organization__name. A template
    describing a list of Policies is used.'''

    template_name = 'policies/policy_text_by_category_by_org_name_list.html'

    if not page_title:
        page_title = policy_type + ' Policies'

    view = ResourceItemListView.as_view(
        model=models.Policy,
        queryset=models.Policy.objects.filter(
            type__type=policy_type).order_by(
            'category', 'organization__name'),
        template_name=template_name)
    if member_only:
        view = members_only(view)
        
    return url(url_string, view, name=slugify(policy_type),
               kwargs={'page_title': page_title,
                       'member_only': member_only })


urlpatterns = patterns('',

    policy_url(
        r'^energy-efficient-appliance-procurement-policies',
        policy_type='Appliance Procurement',
        page_title='Energy Efficient Appliance Procurement Policies',
        with_description=True,
        member_only=True),

    policy_by_country_by_org_name_url(
        url_string=r'^campus-stormwater-policies-plans',
        policy_type='Stormwater',
        page_title='Campus Stormwater Policies / Plans',
        opening_text="""
            This resource lists campus stormwater policies and
            procedures that exist independently of water conservation
            policies, which can be found within general <a
            href="/resources/water-conservation-policies">Campus
            Water Conservation Policies</a>.
            """,
        member_only=True),

    policy_url(url_string=r'^energy-conservation-policies',
               policy_type='Energy Conservation',
               page_title='Campus Sustainable Energy Policies',
               bold_org_name=False),

    policy_url(
        r'^campus-sustainable-procurement-policies',
        policy_type='General Procurement',
        with_description=True,
        page_title='Campus Sustainable Procurement Policies',
        member_only=True),

    policy_by_category_by_org_name_url(
        r'^campus-sustainability-and-environmental-policies',
        policy_type='Sustainability',
        page_title='Campus Sustainability and Environmental Policies',
        member_only=True),

    policy_by_country_by_org_name_url(
        url_string=r'^telecommuting-alternative-work',
        policy_type='Telecommuting',
        page_title='Telecommuting (Alternative Work) Policies',
        opening_text="""This resource is a list of college and
                        university telecommuting policies that
                        facilitate alternative work arrangements for a
                        selection of employees.""",
        member_only=True),

    policy_by_country_by_org_name_url(
        url_string=r'^water-conservation-policies',
        policy_type='Water Conservation',
        opening_text="""This resource lists campus water conservation
                        policies and procedures that exist
                        independently of another policy or plan. More
                        water conservation policies can be found
                        within <a href="/general_policies.php">
                        Campus Sustainability Policies - General</a>.""",
        member_only=True),

    policy_url(
        r'^campus-living-wage-policies',
        policy_type='Living Wage',
        with_description=True,
        page_title='Campus Living Wage Policies',
        member_only=True),

    policy_url(
        r'^campus-anti-idling-policies',
        policy_type='Anti-Idling',
        page_title='Campus Anti-Idling Policies',
        with_description=True,
        member_only=True),

    policy_url(
        r'^paper-procurement-policies',
        policy_type='Paper Procurement',
        page_title='Campus Sustainable Paper Procurement Policies',
        with_description=True,
        member_only=True),

    policy_url(
        r'^integrated-pest-management-policies',
        policy_type='Integrated Pest Management',
        page_title='Campus Integrated Pest Management Policies',
        table_list=True,
        member_only=True),

    policy_url(
        r'^trademark-licensee-code-conduct',
        policy_type='Licensee Code of Conduct',
        page_title='Campus Trademark Licensee Code of Conduct',
        table_list=True,
        member_only=True),

    policy_url(
        r'^campus-recycling-and-waste-minimization-policies',
        policy_type='Recycling',
        page_title='Campus Recycling and Waste Minimization Policies',
        table_list=True,
        opening_text="""This resource compiles campus waste management
                        policies that focus on waste minimization and/or
                        recycling.""",
        member_only=True),

    url(r'^campus-fair-trade-practices-policies',
        view=ResourceItemListView.as_view(
            model=models.FairTradePolicy,
            queryset=models.FairTradePolicy.objects.order_by(
                    'organization__country', 'organization__name')),
        name='fair-trade',
        kwargs={'member_only': True, 'title': 'Campus Fair Trade Practices and Policies'}),

    url(r'^socially-responsible-investment-policies',
        view=ResourceItemListView.as_view(
            model=models.ResponsibleInvestmentPolicy,
            queryset=models.ResponsibleInvestmentPolicy.objects.order_by(
                    'investment_type', 'organization__name')),
            name='responsible-investment',
            kwargs={'member_only': True, 'title': 'Socially Responsible Investment Policies'}),

    url(r'^campus-building-guidelines-and-green-building-policies',
        view=ResourceItemListView.as_view(
            model=models.GreenBuildingPolicy,
            queryset=models.GreenBuildingPolicy.objects.order_by(
                    'leed_level', 'organization__name')),
            name='green-building',
            kwargs={'member_only': True,
                    'title': 'Campus Building Guidelines & Green Building Policies',
                    'type_list': [ level[0] for level in
                                   models.GreenBuildingPolicy.LEED_LEVELS ],
                    'type_dict': dict(models.GreenBuildingPolicy.LEED_LEVELS)}),
    )
