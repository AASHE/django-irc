from base import PageParser, SimpleTableParser
from BeautifulSoup import BeautifulSoup, NavigableString


class ApplianceProcurement(PageParser):
    '''
    >>> parser = ApplianceProcurement()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    >>> parser.data[0]['description'] != ''
    True
    '''
    url = 'http://www.aashe.org/resources/energy-efficient-appliance-procurement-policies'
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
            data['institution'] = textEl
            data['title'] = anchor.text
            data['url'] = dict(anchor.attrs).get('href', '')
            self.data.append(data)
            data = {}

class SustainbilityPolicies(PageParser):
    '''
    >>> parser = SustainbilityPolicies()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-sustainability-and-environmental-policies'
    login_required = True
    
    def parsePage(self):
        anchors = self.soup.find('div', {'class': 'content clear-break'}).findAll('a')
        data = {}
        for anchor in anchors:
            textEl = anchor.findPrevious(text=True)
            data['institution'] = textEl
            data['title'] = anchor.text
            data['url'] = dict(anchor.attrs).get('href', '')
            data['category'] = anchor.getPrevious('h2').text
            self.data.append(data)
            data = {}
            
class CampusFairTrade(PageParser):
    '''
    >>> parser = CampusFairTrade()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''                    
    url = 'http://www.aashe.org/resources/campus-fair-trade-practices-policies'
    login_required = True

    def parsePage(self):
        tables = self.soup.findAll('table')
        # first table is Canada
        policyData = {}
        for row in tables[0].findAll('tr')[1:]:
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs).get('href', '')
            policyData['title'] = tags[3].text
            policyData['product_types'] = tags[5].text
            policyData['country'] = 'Canada'
            self.data.append(policyData)
            policyData = {}

        # second table is United States
        for row in tables[1].findAll('tr')[1:]:
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs).get('href', '')
            policyData['title'] = tags[3].text
            policyData['product_types'] = tags[5].text            
            policyData['country'] = 'United States of America'
            self.data.append(policyData)
            policyData = {}
