from base import ElectronicWasteParser, PageParser, SimpleTableParser
from rc.resources.apps.policies import models

BASE_URL = 'http://www.aashe.org/resources/'


class SimplePolicyTableParser(SimpleTableParser):
    '''Pushes a policy type into a SimpleTableParser's data dictionary.'''

    def type_policies(self):
        for policy in self.data:
            policy['policy_type'] = self.policy_type

    def parsePage(self):
        super(SimplePolicyTableParser, self).parsePage()
        self.type_policies()


class PolicyPageParser(PageParser):
    '''Pushes a policy type into a PageParser's data dictionary.'''

    def type_policies(self):
        for policy in self.data:
            policy['policy_type'] = self.policy_type

    def parsePage(self):
        super(PolicyPageParser, self).parsePage()
        self.type_policies()


class IntegratedPestPolicies(SimplePolicyTableParser):
    '''
    >>> parser=IntegratedPestPolicies()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'integrated-pest-management-policies'
    login_required = True
    policy_type = 'Integrated Pest Management'


class LicenseeCodeConductPolicies(SimplePolicyTableParser):
    '''
    >>> parser=LicenseeCodeConduct()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'trademark-licensee-code-conduct'
    login_required = True
    policy_type = 'Licensee Code of Conduct'


class GreenCleaningPolicies(SimplePolicyTableParser):
    '''
    >>> parser = GreenCleaning()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'green-cleaning'
    login_required = True
    policy_type = 'Green Cleaning'

    def parsePage(self):
        # Only the 2nd table has policy info.
        self.processTable(self.soup.findAll('table')[1])
        self.type_policies()


class RecyclingPolicies(SimplePolicyTableParser):
    '''
    >>> parser = RecyclingPolicy()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-recycling-and-waste-minimization-policies'
    login_required = True
    policy_type = 'Recycling'


class ApplianceProcurementPolicies(PolicyPageParser):
    '''
    >>> parser = ApplianceProcurement()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    >>> parser.data[0]['description'] != ''
    True
    '''
    url = BASE_URL + 'energy-efficient-appliance-procurement-policies'
    login_required = True
    policy_type = 'Appliance Procurement'

    def parsePage(self):
        paras = self.soup.find('div',
                               {'class': 'content clear-block'}).findAll('p')
        data = {}
        for para in paras:
            strong = para.find('strong')
            anchor = para.find('a')
            br = para.find('br')
            textEl = br.nextSibling
            data['title'] = anchor.text
            data['url'] = dict(anchor.attrs).get('href', '')
            data['description'] = textEl
            data['institution'] = strong.text
            self.data.append(data)
            data = {}
        self.type_policies()


class GeneralProcurementPolicies(PolicyPageParser):
    '''
    >>> parser = GeneralProcurement()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    >>> parser.data[0]['description'] != ''
    True
    '''
    url = BASE_URL + 'campus-sustainable-procurement-policies'
    login_required = True
    policy_type = 'General Procurement'

    def parsePage(self):
        paras = self.soup.findAll('p')[:-1]
        policyData = {}
        for p in paras:
            try:
                nodes = [el for el in p]
                policyData['title'] = nodes[2].text
                policyData['url'] = dict(nodes[2].attrs).get('href', '')
                policyData['institution'] = nodes[0].text
                policyData['notes'] = nodes[4].title()
                self.data.append(policyData)
                policyData = {}
            except:
                continue
        self.type_policies()


class LivingWagePolicies(PolicyPageParser):
    '''
    >>> parser = LivingWage()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    >>> parser.data[0]['description'] != ''
    True
    '''
    url = BASE_URL + 'campus-living-wage-policies'
    login_required = True
    policy_type = 'Living Wage'

    def parsePage(self):
        paras = self.soup.find('div',
                               {'class': 'content clear-block'}).findAll('p')
        data = {}
        for para in paras:
            strong = para.find('strong')
            anchor = para.find('a')
            br = para.find('br')
            textEl = br.nextSibling
            data['title'] = anchor.text
            data['url'] = dict(anchor.attrs).get('href', '')
            data['description'] = textEl
            data['institution'] = strong.text
            self.data.append(data)
            data = {}
        self.type_policies()


class AntiIdlingPolicies(PolicyPageParser):
    '''
    >>> parser = AntiIdling()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    >>> parser.data[0]['description'] != ''
    True
    '''
    url = BASE_URL + 'campus-anti-idling-policies'
    login_required = True
    policy_type = 'Anti-Idling'

    def parsePage(self):
        paras = self.soup.find('div',
                               {'class': 'content clear-block'}).findAll('p')
        data = {}
        for para in paras:
            strong = para.find('strong')
            anchor = para.find('a')
            br = para.find('br')
            textEl = br.nextSibling
            data['title'] = anchor.text
            data['url'] = dict(anchor.attrs).get('href', '')
            data['description'] = textEl
            data['institution'] = strong.text
            self.data.append(data)
            data = {}
        self.type_policies()


class PaperProcurementPolicies(PolicyPageParser):
    '''
    >>> parser = PaperProcurement()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    >>> parser.data[0]['description'] != ''
    True
    '''
    url = BASE_URL + 'paper-procurement-policies'
    login_required = True
    policy_type = 'Paper Procurement'

    def parsePage(self):
        paras = self.soup.find('div',
                               {'class': 'content clear-block'}).findAll('p')
        data = {}
        for para in paras:
            strong = para.find('strong')
            anchor = para.find('a')
            br = para.find('br')
            textEl = br.nextSibling
            data['title'] = anchor.text
            data['url'] = dict(anchor.attrs).get('href', '')
            data['description'] = textEl
            data['institution'] = strong.text
            self.data.append(data)
            data = {}
        self.type_policies()


class StormwaterPolicies(SimplePolicyTableParser):
    '''
    >>> parser = StormwaterPolicies()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    >>> parser.data[0]['country'] in ('United States', 'Australia')    True
    '''
    url = BASE_URL + 'campus-stormwater-policies-plans'
    login_required = True
    policy_type = 'Stormwater'

    def parsePage(self, headings=True):
        for table in self.soup.findAll('table')[0:2]:
            self.processTable(table, headings=headings)
        self.type_policies()


class ResponsibleInvestmentPolicies(SimplePolicyTableParser):
    '''
    >>> parser = ResponsibleInvestmentPolicies()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'socially-responsible-investment-policies'
    login_required = True
    policy_type = 'Responsible Investment'

    def processTable(self, table, headings, investment_type):
        policies = super(ResponsibleInvestmentPolicies, self).processTable(
            table=table, headings=headings, save_resources=False)
        for policy in policies:
            policy['investment_type'] = investment_type
        self.data.extend(policies)

    def parsePage(self):
        for table in self.soup.findAll('table'):
            investment_type = table.findPrevious('h2').text
            self.processTable(table=table, headings=True,
                              investment_type=investment_type)
        self.type_policies()


class EnergyConservationPolicies(PolicyPageParser):
    '''
    >>> parser = EnergyConservationPolicies()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'energy-conservation-policies'
    login_required = True
    policy_type = 'Energy Conservation'

    def parsePage(self):
        para = self.soup.find('div', {'class': 'content clear-block'}).find('p')
        data = {}
        for br in para.findAll('br'):
            anchor = br.previousSibling
            textEl = br.previousSibling.previousSibling
            data['institution'] = textEl.strip(' - ')
            data['title'] = anchor.text
            data['url'] = dict(anchor.attrs).get('href', '')
            self.data.append(data)
            data = {}
        self.type_policies()


class GeneralSustainabilityPolicies(PolicyPageParser):
    '''
    >>> parser = SustainbilityPolicies()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-sustainability-and-environmental-policies'
    login_required = True
    policy_type = 'Sustainability'

    def parsePage(self):
        anchors = self.soup.find('div',
                                 {'class': 'content clear-block'}).findAll('a')
        data = {}
        for anchor in anchors:
            textEl = anchor.findPrevious(text=True)
            data['institution'] = textEl.strip(' - ')
            data['title'] = anchor.text
            data['url'] = dict(anchor.attrs).get('href', '')
            data['category'] = anchor.findPrevious('h2').text
            self.data.append(data)
            data = {}
        self.type_policies()


class CampusFairTradePolicies(SimplePolicyTableParser):
    '''
    >>> parser = CampusFairTrade()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-fair-trade-practices-policies'
    login_required = True
    policy_type = 'Campus Fair Trade'

    def processTableData(self, row):
        policies = super(CampusFairTradePolicies, self).processTableData(row)
        cells = row.findAll('td')
        product_types = cells[-1].text
        for policy in policies:
            policy['product_types'] = product_types
        return policies

    def parsePage(self, headings=True):
        for table in self.soup.findAll('table'):
            self.processTable(table, headings=headings)
        self.type_policies()


class TelecommutingPolicies(PolicyPageParser):
    '''
    >>> parser = TelecommutingPolicy()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    TRUE
    '''
    url = BASE_URL + 'telecommuting-alternative-work'
    login_required = True
    policy_type = 'Telecommuting'

    def parsePage(self):
        headers = self.soup.find('div',
                                 {'class': 'content clear-block'}).findAll('h2')
        data = {}
        for header in headers:
            row_tags = header.nextSibling.nextSibling.findAll('tr')[1:]
            for row in row_tags:
                tags = [el for el in row]
                data['country'] = header.text
                data['institution'] = tags[1].text
                data['url'] = dict(tags[3].find('a').attrs).get('href', '')
                data['title'] = tags[3].text
                self.data.append(data)
                data = {}
        self.type_policies()


class WaterConservationPolicies(SimplePolicyTableParser):
    '''
    >>> parser = WaterConservationPolicy()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    TRUE
    '''
    url = BASE_URL + 'water-conservation-policies'
    login_required = True
    policy_type = 'Water Conservation'

    def parsePage(self):
        content_div = self.soup.find('div',
                                     {'class': 'content clear-block'})
        tables = content_div.findAll('table')
        for table in tables:
            self.processTable(table, headings=True)
        self.type_policies()


class GreenBuildingPolicies(PolicyPageParser):
    url = BASE_URL + 'campus-building-guidelines-and-green-building-policies'
    login_required = True
    policy_type = 'Green Building'

    def parsePage(self):
        content_block = self.soup.find('div',
                                       {'class': 'content clear-block'})
        for para in content_block.find('h2').findNextSiblings('p'):
            policy = {}
            policy['institution'] = para.find('strong').extract().text
            anchor = para.find('a').extract()
            policy['url'] = anchor['href']
            policy['title'] = anchor.text
            policy['description'] = para.text.strip('- ')
            standard_description = para.findPrevious('h2').text
            for level in models.GreenBuildingPolicy.LEED_LEVELS:
                if level[1] in standard_description:
                    policy['leed_level'] = level[0]
            self.data.append(policy)
        self.type_policies()


class ElectronicWastePolicies(ElectronicWasteParser):

    policy_type = 'Electronic Waste'

    def parsePage(self):
        super(ElectronicWastePolicies, self).parsePage('policies')
        for policy in self.data:
            policy['policy_type'] = self.policy_type
