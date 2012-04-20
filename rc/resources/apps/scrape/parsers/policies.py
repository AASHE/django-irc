from base import PageParser, SimpleTableParser
from rc.resources.apps.policies import models


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
    url = 'http://www.aashe.org/resources/integrated-pest-management-policies'
    login_required = True
    policy_type = 'Integrated Pest Management'


class LicenseeCodeConductPolicies(SimplePolicyTableParser):
    '''
    >>> parser=LicenseeCodeConduct()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/trademark-licensee-code-conduct'
    login_required = True
    policy_type = 'Licensee Code of Conduct'


class GreenCleaningPolicies(SimplePolicyTableParser):
    '''
    >>> parser = GreenCleaning()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/green-cleaning'
    login_required = True
    policy_type = 'Green Cleaning'

    def parsePage(self):
        # parent method will get the data from the first table and
        # stuff it into self.data
        super(GreenCleaningPolicies, self).parsePage()
        # parse the data from the second table and stuff into self.data
        self.processTable(self.soup.findAll('table')[1])
        self.type_policies()


class RecyclingPolicies(SimplePolicyTableParser):
    '''
    >>> parser = RecyclingPolicy()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-recycling-and-waste-minimization-policies'
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
    url = ('http://www.aashe.org/resources/'
           'energy-efficient-appliance-procurement-policies')
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
    url = ('http://www.aashe.org/resources/'
           'campus-sustainable-procurement-policies')
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
    url = 'http://www.aashe.org/resources/campus-living-wage-policies'
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
    url = 'http://www.aashe.org/resources/campus-anti-idling-policies'
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
    url = 'http://www.aashe.org/resources/paper-procurement-policies'
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
    >>> parser.data[0]['country'] in ('United States', 'Australia')
    True
    '''
    url = 'http://www.aashe.org/resources/campus-stormwater-policies-plans'
    login_required = True
    policy_type = 'Stormwater'

    def processTableData(self, row, els):
        '''
        row - the <tr> element
        tags - the elements inside the <tr> element
        '''
        data = {}
        data['institution'] = els[1].text
        data['title'] = els[3].text
        data['url'] = dict(els[3].find('a').attrs).get('href', '')
        data['country'] = row.findPrevious('h2').text
        return data

    def parsePage(self, headings=True):
        # data is in the first <table> on the page
        self.processTable(self.soup.findAll('table')[0], headings=headings)
        # data is in the second <table> on the page
        self.processTable(self.soup.findAll('table')[1], headings=headings)
        self.type_policies()


class ResponsibleInvestmentPolicies(SimplePolicyTableParser):
    '''
    >>> parser = ResponsibleInvestmentPolicies()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    >>> parser.data[0]['type'] in ('Independent Policies on Responsible Investment',
     'Overall Investment Policies that Include Sustainability Considerations', 'Policies and Special Funds Managed by Students')
    True
    '''
    url = 'http://www.aashe.org/resources/socially-responsible-investment-policies'
    login_required = True
    policy_type = 'Responsible Investment'

    def processTableData(self, row, els):
        '''
        row - the <tr> element
        tags - the elements inside the <tr> element
        '''
        data = {}
        data['institution'] = els[1].text
        data['title'] = els[3].text
        data['url'] = dict(els[3].find('a').attrs).get('href', '')
        data['investment_type'] = row.findPrevious('h2').text
        return data

    def parsePage(self, headings=True):
        for table in self.soup.findAll('table'):
            self.processTable(table, headings=headings)
        self.type_policies()


class EnergyConservationPolicies(PolicyPageParser):
    '''
    >>> parser = EnergyConservationPolicies()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/energy-conservation-policies'
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
    url = 'http://www.aashe.org/resources/campus-sustainability-and-environmental-policies'
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
    url = 'http://www.aashe.org/resources/campus-fair-trade-practices-policies'
    login_required = True
    policy_type = 'Campus Fair Trade'

    def processTableData(self, row, els):
        policyData = super(CampusFairTradePolicies,
                           self).processTableData(row, els)
        policyData['product_types'] = els[5].text
        return policyData

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
    url = 'http://www.aashe.org/resources/telecommuting-alternative-work'
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


class WaterConservationPolicies(PolicyPageParser):
    '''
    >>> parser = WaterConservationPolicy()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    TRUE
    '''
    url = 'http://www.aashe.org/resources/water-conservation-policies'
    login_required = True
    policy_type = 'Water Conservation'

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


class GreenBuildingPolicies(PolicyPageParser):
    url = ('http://www.aashe.org/resources/'
           'campus-building-guidelines-and-green-building-policies')
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


class ElectronicWastePolicies(SimplePolicyTableParser):
    '''
    >>> parser=ElectronicWaste()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/e-waste-programs-policies-and-events'
    login_required = True
    policy_type = 'Electronic Waste'

    def processTableData(self, row, els):
        '''
        row - the <tr> element
        tags - the elements inside the <tr> element
        '''
        data = {}
        data['institution'] = els[1].text
        data['title'] = els[3].text
        data['url'] = dict(els[3].find('a').attrs).get('href', '')
        data['country'] = row.findPrevious('h2').text
        return data

    def parsePage(self, headings=True):
        def header_texts(table):
            headers = table.findAll('th')
            return [ h.lower() for h in headers ]
        tables = self.soup.findAll('table')
        policies_table = [ t for t in tables
                           if 'policies' in header_texts(t) ][0]
        self.processTable(policies_table, headings=headings)
        self.type_policies()
