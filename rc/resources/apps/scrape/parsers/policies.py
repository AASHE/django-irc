from base import PageParser, SimpleTableParser
from rc.resources.apps.policies import models


class IntegratedPestPolicies(SimpleTableParser):
    '''
    >>> parser=IntegratedPestPolicies()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/integrated-pest-management-policies'
    login_required = True

class LicenseeCodeConduct(SimpleTableParser):
    '''
    >>> parser=LicenseeCodeConduct()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/trademark-licensee-code-conduct'
    login_required = True

class GreenCleaning(SimpleTableParser):
    '''
    >>> parser = GreenCleaning()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/green-cleaning'
    login_required = True

    def parsePage(self):
        # parent method will get the data from the first table and stuff it into self.data
        super(GreenCleaning, self).parsePage()
        # parse the data from the second table and stuff into self.data
        self.processTable(self.soup.findAll('table')[1])

class RecyclingPolicy(SimpleTableParser):
    '''
    >>> parser = RecyclingPolicy()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-recycling-and-waste-minimization-policies'
    login_required = True

class ApplianceProcurement(PageParser):
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

    def parsePage(self):
        paras = self.soup.find('div', {'class': 'content clear-block'}).findAll('p')
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

class GeneralProcurement(PageParser):
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

class LivingWage(PageParser):
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

    def parsePage(self):
        paras = self.soup.find('div', {'class': 'content clear-block'}).findAll('p')
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

class AntiIdling(PageParser):
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

    def parsePage(self):
        paras = self.soup.find('div', {'class': 'content clear-block'}).findAll('p')
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

class PaperProcurement(PageParser):
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

    def parsePage(self):
        paras = self.soup.find('div', {'class': 'content clear-block'}).findAll('p')
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

class StormwaterPolicies(SimpleTableParser):
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

class ResponsibleInvestmentPolicies(SimpleTableParser):
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

class EnergyConservationPolicies(PageParser):
    '''
    >>> parser = EnergyConservationPolicies()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/energy-conservation-policies'
    login_required = True

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

class GeneralSustainabilityPolicies(PageParser):
    '''
    >>> parser = SustainbilityPolicies()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-sustainability-and-environmental-policies'
    login_required = True

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

class CampusFairTrade(SimpleTableParser):
    '''
    >>> parser = CampusFairTrade()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-fair-trade-practices-policies'
    login_required = True

    def processTableData(self, row, els):
        policyData = super(CampusFairTrade, self).processTableData(row, els)
        policyData['product_types'] = els[5].text
        return policyData

    def parsePage(self, headings=True):
        for table in self.soup.findAll('table'):
            self.processTable(table, headings=headings)

class TelecommutingPolicy(PageParser):
    '''
    >>> parser = TelecommutingPolicy()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    TRUE
    '''
    url = 'http://www.aashe.org/resources/telecommuting-alternative-work'
    login_required = True

    def parsePage(self):
        headers = self.soup.find('div', {'class': 'content clear-block'}).findAll('h2')
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

class WaterConservationPolicy(PageParser):
    '''
    >>> parser = WaterConservationPolicy()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    TRUE
    '''
    url = 'http://www.aashe.org/resources/water-conservation-policies'
    login_required = True

    def parsePage(self):
        headers = self.soup.find('div', {'class': 'content clear-block'}).findAll('h2')
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

class GreenBuildingPolicies(PageParser):
    url = ('http://www.aashe.org/resources/'
           'campus-building-guidelines-and-green-building-policies')
    login_required = True

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

class ElectronicWaste(SimpleTableParser):
    '''
    >>> parser=ElectronicWaste()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/e-waste-programs-policies-and-events'
    login_required = True

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
