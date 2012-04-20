from django.conf.urls.defaults import patterns, url
from django.template.defaultfilters import slugify

from rc.resources.views import ResourceItemListView, \
     handle_missing_organizations
from rc.resources.apps.policies import models


def url_name(surname):
    for tag in ('policy', 'policies'):
        surname = surname.replace('-' + tag, '')
    return 'resources:policies:' + surname

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

    return url(url_string,
               ResourceItemListView.as_view(
                   model=models.Policy,
                   queryset=models.Policy.objects.filter(
                       type__type=policy_type).order_by('organization__name'),
                   template_name=template_name),
                name=url_name(slugify(policy_type)),
                kwargs={'page_title': page_title,
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

    return url(url_string,
               ResourceItemListView.as_view(
                    model=models.Policy,
                    queryset=models.Policy.objects.filter(
                        type__type=policy_type).order_by(
                            'organization__country', 'organization__name'),
                    template_name=template_name),
                name=url_name(slugify(policy_type)),
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

    return url(url_string,
               ResourceItemListView.as_view(
                    model=models.Policy,
                    queryset=models.Policy.objects.filter(
                        type__type=policy_type).order_by(
                            'category', 'organization__name'),
                    template_name=template_name),
                    name=url_name(slugify(policy_type)),
                    kwargs={'page_title': page_title,
                            'member_only': member_only })


urlpatterns = patterns('',

    policy_url(
        r'^resources/energy-efficient-appliance-procurement-policies',
        policy_type='Appliance Procurement',
        with_description=True,
        member_only=True),

    policy_by_country_by_org_name_url(
        url_string=r'^resources/campus-stormwater-policies-plans',
        policy_type='Stormwater',
        page_title='Campus Stormwater Policies / Plans',
        opening_text="""
            This resource lists campus stormwater policies and
            procedures that exist independently of water conservation
            policies, which can be found within general <a
            href="/resources/campus-water-conservation-policies">Campus
            Water Conservation Policies</a>.
            """,
        member_only=True),

    policy_url(url_string=r'^resources/energy-conservation-policies',
               policy_type='Energy Conservation',
               page_title='Campus Sustainable Energy Policies',
               bold_org_name=False),

    policy_url(
        r'^resources/campus-sustainable-procurement-policies',
        policy_type='General Procurement',
        with_description=True,
        page_title='Campus Sustainable Procurement Policies',
        member_only=True),

    policy_by_category_by_org_name_url(
        r'^resources/campus-sustainability-and-environmental-policies',
        policy_type='Sustainability',
        page_title='Campus Sustainability and Environmental Policies',
        member_only=True),

    policy_by_country_by_org_name_url(
        url_string=r'^resources/telecommuting-alternative-work',
        policy_type='Telecommuting',
        page_title='Telecommuting (Alternative Work) Policies',
        opening_text="""This resource is a list of college and
                        university telecommuting policies that
                        facilitate alternative work arrangements for a
                        selection of employees.""",
        member_only=True),

    policy_by_country_by_org_name_url(
        url_string=r'^resources/water-conservation-policies',
        policy_type='Water Conservation',
        opening_text="""This resource lists campus water conservation
                        policies and procedures that exist
                        independently of another policy or plan. More
                        water conservation policies can be found
                        within <a href="/resources/general_policies.php">
                        Campus Sustainability Policies - General</a>.""",
        member_only=True),

    policy_url(
        r'^resources/campus-living-wage-policies',
        policy_type='Living Wage',
        with_description=True,
        page_title='Campus Living Wage Policies',
        member_only=True),

    policy_url(
        r'^resources/campus-anti-idling-policies',
        policy_type='Anti-Idling',
        with_description=True,
        member_only=True),

    policy_url(
        r'^resources/paper-procurement-policies',
        policy_type='Paper Procurement',
        page_title='Paper Procurement Policies',
        with_description=True,
        member_only=True),

    policy_url(
        r'^resources/integrated-pest-management-policies',
        policy_type='Integrated Pest Management',
        page_title='Integrated Pest Management Policies',
        table_list=True,
        member_only=True),

    policy_url(
        r'^resources/trademark-licensee-code-conduct',
        policy_type='Licensee Code of Conduct',
        page_title='Trademark Licensee Code of Conduct',
        table_list=True,
        member_only=True),

    policy_url(
        r'^resources/campus-recycling-and-waste-minimization-policies',
        policy_type='Recycling',
        page_title='Campus Recycling and Waste Minimization Policies',
        table_list=True,
        opening_text="""This resource compiles campus waste management
                        policies that focus on waste minimization and/or
                        recycling.""",
        member_only=True),

    url(r'^resources/campus-fair-trade-practices-policies',
        view=ResourceItemListView.as_view(
            model=models.FairTradePolicy,
            queryset=handle_missing_organizations(
                models.FairTradePolicy.objects.order_by(
                    'organization__country', 'organization__name'))),
        name=url_name('fair-trade'),
        kwargs={'member_only': True}),

    url(r'^resources/socially-responsible-investment-policies',
        view=ResourceItemListView.as_view(
            model=models.ResponsibleInvestmentPolicy,
            queryset=handle_missing_organizations(
                models.ResponsibleInvestmentPolicy.objects.order_by(
                    'investment_type', 'organization__name'))),
            name=url_name('responsible-investment'),
            kwargs={'member_only': True}),

    url(r'^resources/campus-building-guidelines-and-green-building-policies',
        view=ResourceItemListView.as_view(
            model=models.GreenBuildingPolicy,
            queryset=handle_missing_organizations(
                models.GreenBuildingPolicy.objects.order_by(
                    'leed_level', 'organization__name'))),
            name=url_name('green-building'),
            kwargs={'member_only': True,
                    'type_list': [ level[0] for level in
                                   models.GreenBuildingPolicy.LEED_LEVELS ],
                    'type_dict': dict(models.GreenBuildingPolicy.LEED_LEVELS)}),



    )
