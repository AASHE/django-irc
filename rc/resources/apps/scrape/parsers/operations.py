from base import PageParser, SimpleTableParser
from BeautifulSoup import BeautifulSoup, NavigableString


class RecyclingWasteMinimization(SimpleTableParser):
    '''
    >>> parser = RecyclingWasteMinimization()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-recycling-and-waste-minimization-websites'
    login_required = True

class CampusComposting(SimpleTableParser):
    '''
    >>> parser = CampusComposting()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''    
    url = 'http://www.aashe.org/resources/campus-composting-programs'
    login_required = True

class GeneralProcurementPolicies(PageParser):
    '''
    >>> parser = GeneralProcurementPolicies()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''        
    url = 'http://www.aashe.org/resources/campus-sustainable-procurement-policies'
    login_required = True

    def parsePage(self):
        paras = self.soup.findAll('p')[:-1]
        policyData = {}
        for p in paras:
            try:
                nodes = [el for el in p]
                policyData['policy_name'] = nodes[2].text
                policyData['url'] = dict(nodes[2].attrs).get('href', '')
                policyData['institution'] = nodes[0].text
                policyData['notes'] = nodes[4].title()
                self.data.append(policyData)
                policyData = {}
            except:
                continue    

class EnergyPoliciesParser(PageParser):
    '''
    >>> parser = EnergyPoliciesParser()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/energy-conservation-policies'

    def parsePage(self):
        # policies listing starts at first paragraph tag on the page
        para = self.soup.findAll('p')[0]
        # each policy line is separated by a <br/> tag... loop until we hit one...
        elements = [el for el in para]
        policyData = {}
        for el in elements:
            tag = getattr(el, 'name', None)
            if tag == 'br':
                self.data.append(policyData)
                policyData = {}
                continue
            elif tag == 'a':
                # anchor tag means it's a link...
                linkText = el.text
                url = dict(el.attrs).get('href', None)
                policyData.update({'url': url, 'policy_name': linkText})
            elif isinstance(el, NavigableString) and '(pdf)' not in el.title().lower():
                # not a <br/> and not an <a> so it's probably the school name text
                # split on the '-' separator and strip of lead/trail whitespace...
                institution = el.title().rsplit('-', 1)[0].strip()
                policyData['institution'] = institution
            
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
    url = 'http://www.aashe.org/resources/waste_policies.php'
    login_required = True
            
class SurplusProperty(SimpleTableParser):
    '''
    >>> parser = SurplusProperty()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''        
    url = 'http://www.aashe.org/resources/campus-surplus-recycling'
    login_required = True

    def parsePage(self):
        tables = self.soup.findAll('table')
        # first table is 'Canada'
        policyData = {}
        for row in tables[0].findAll('tr')[1:]:
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs)['href']
            policyData['policy_name'] = tags[3].text
            policyData['country'] = 'Canada'
            self.data.append(policyData)
            policyData = {}
            
        # second table is overall
        for row in tables[0].findAll('tr')[1:]:
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs)['href']
            policyData['policy_name'] = tags[3].text
            policyData['country'] = 'United States of America'
            self.data.append(policyData)
            policyData = {}

class BottledWaterBans(PageParser):
    '''
    >>> parser = BottledWaterBans()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''            
    url = 'http://www.aashe.org/resources/bottled-water-elimination-and-reduction'
    login_required = True

    def parsePage(self):
        tables = self.soup.findAll('table')
        # first table is 'Campus-wide bans'
        policyData = {}
        for row in tables[0].findAll('tr'):
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs).get('href', '')
            policyData['title'] = tags[3].text
            policyData['type'] = 'Campus-Wide Bans'
            self.data.append(policyData)
            policyData = {}

        # second table is Area, School and Department Specific Bans
        for row in tables[1].findAll('tr'):
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs).get('href', '')
            policyData['title'] = tags[3].text
            policyData['type'] = 'Area, School and Department Specific Bans'
            self.data.append(policyData)
            policyData = {}

        # third table is Student Campaigns to Ban Bottled Water
        for row in tables[2].findAll('tr'):
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs).get('href', '')
            policyData['title'] = tags[3].text
            policyData['type'] = 'Student Campaigns to Ban Bottled Water'
            self.data.append(policyData)
            policyData = {}

        # fourth table is Awareness and Reduction Campaigns
        for row in tables[3].findAll('tr'):
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs).get('href', '')
            policyData['title'] = tags[3].text
            policyData['type'] = 'Awareness and Reduction Campaigns'
            self.data.append(policyData)
            policyData = {}
        
class SustainableDiningInitiatives(PageParser):
    '''
    >>> parser = SustainableDiningInitiatives()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''                
    url = 'http://www.aashe.org/resources/sustainable-dining-initiatives-campus'
    login_required = True

    def parsePage(self):
        headers = self.soup.find('div', {'class': 'content clear-block'}).findAll('h2')
        policyData = {}
        for header in headers:
            para = header.nextSibling.nextSibling
            elements = [el for el in para]
            for el in elements:
                tag = getattr(el, 'name', None)
                if tag == 'br':
                    policyData['type'] = header.text
                    self.data.append(policyData)
                    policyData = {}
                    continue
                elif tag == 'a':
                    linkText = el.text
                    url = dict(el.attrs).get('href', '')
                    policyData.update({'url': url, 'policy_name': linkText})
                elif isinstance(el, NavigableString) and '(article)' not in el.title().lower() and '**' not in el.title().lower():
                    institution = el.title().rsplit('-', 1)[0].strip()
                    policyData['institution'] = institution


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
            policyData['policy_name'] = tags[3].text
            policyData['product_types'] = tags[5].text
            policyData['country'] = 'Canada'
            self.data.append(policyData)
            policyData = {}

        # second table is United States
        for row in tables[1].findAll('tr')[1:]:
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs).get('href', '')
            policyData['policy_name'] = tags[3].text
            policyData['product_types'] = tags[5].text            
            policyData['country'] = 'United States of America'
            self.data.append(policyData)
            policyData = {}

class SustainabilityPurchasing(PageParser):
    '''
    >>> parser = SustainabilityPurchasing()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''                        
    url = 'http://www.aashe.org/resources/links-related-sustainable-purchasing-campus'
    login_required = True

    def parsePage(self):
        headers = self.soup.find('div', {'class': 'content clear-block'}).findAll('h2')
        policyData = {}
        for header in headers:
            para = header.nextSibling.nextSibling
            elements = [el for el in para]
            for el in elements:
                tag = getattr(el, 'name', None)
                if tag == 'br':
                    policyData['type'] = header.text
                    self.data.append(policyData)
                    policyData = {}
                    continue
                elif tag == 'a':
                    linkText = el.text
                    url = dict(el.attrs).get('href', '')
                    policyData.update({'url': url, 'policy_name': linkText})
                elif isinstance(el, NavigableString) and '(article)' not in el.title().lower() and '**' not in el.title().lower():
                    institution = el.title().rsplit('-', 1)[0].strip()
                    policyData['institution'] = institution

class AlternativeTransport(PageParser):
    '''
    >>> parser = AlternativeTransport()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''                            
    url = 'http://www.aashe.org/resources/campus-alternative-transportation-websites'
    login_required = True

    def parsePage(self):
        para = self.soup.find('div', {'class': 'content clear-block'}).findAll('p')[1]
        nodes = [el for el in para]
        policyData = {}
        for el in nodes:
            tag = getattr(el, 'name', None)
            if tag == 'br':
                self.data.append(policyData)
                policyData = {}
                continue
            elif tag == 'a':
                linkText = el.text
                url = dict(el.attrs).get('href', None)
                policyData.update({'url': url, 'policy_name': linkText})
            elif isinstance(el, NavigableString):
                institution = el.title().rsplit('-', 1)[0].strip()
                policyData['institution'] = institution

class UniversalAccess(PageParser):
    '''
    >>> parser = UniversalAccess()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''                                
    url = 'http://www.aashe.org/resources/campus-universal-transit-passes'
    login_required = False

    def parsePage(self):
        tables = self.soup.findAll('table')
        # first table is Universal Bus/Transit Pass Programs for Canada
        policyData = {}
        for row in tables[0].findAll('tr'):
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs).get('href', '')
            policyData['policy_name'] = tags[3].text
            policyData['type'] = 'Universal Bus/Transit Pass Programs'
            policyData['country'] = 'Canada'
            self.data.append(policyData)
            policyData = {}
        
        # second table is Universal Bus/Transit Pass Programs for USA
        policyData = {}
        for row in tables[1].findAll('tr'):
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs).get('href', '')
            policyData['policy_name'] = tags[3].text
            policyData['type'] = 'Universal Bus/Transit Pass Programs'
            policyData['country'] = 'United States of America'
            self.data.append(policyData)
            policyData = {}

        # third table is Bus/Transit Pass Discount Programs for Canada
        policyData = {}
        for row in tables[2].findAll('tr'):
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs).get('href', '')
            policyData['policy_name'] = tags[3].text
            policyData['type'] = 'Bus/Transit Pass Discount Programs'
            policyData['country'] = 'Canada'
            self.data.append(policyData)
            policyData = {}

        # fourth table is Bus/Transit Pass Discount Programs for USA
        policyData = {}
        for row in tables[3].findAll('tr'):
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs).get('href', '')
            policyData['policy_name'] = tags[3].text
            policyData['type'] = 'Bus/Transit Pass Discount Programs'
            policyData['country'] = 'United States of America'
            self.data.append(policyData)
            policyData = {}

class BicycleSharing(PageParser):
    '''
    >>> parser = BicycleSharing()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''                                    
    url = 'http://www.aashe.org/resources/bicycle-share-programs'
    login_required = True

    def parsePage(self):
        tables = self.soup.findAll('table')
        # first table is Free Bicycle Share Programs in Canada
        policyData = {}
        for row in tables[0].findAll('tr'):
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs).get('href', '')
            policyData['policy_name'] = tags[3].text
            policyData['type'] = 'Free Bicycle Share Programs'
            policyData['country'] = 'Canada'
            self.data.append(policyData)
            policyData = {}

        # second table is Free Bicycle Share Programs in Colombia
        policyData = {}
        for row in tables[1].findAll('tr'):
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs).get('href', '')
            policyData['policy_name'] = tags[3].text
            policyData['type'] = 'Free Bicycle Share Programs'
            policyData['country'] = 'Colombia'
            self.data.append(policyData)
            policyData = {}

        # third table is Free Bicycle Share Programs in USA
        policyData = {}
        for row in tables[2].findAll('tr'):
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs).get('href', '')
            policyData['policy_name'] = tags[3].text
            policyData['type'] = 'Free Bicycle Share Programs'
            policyData['country'] = 'United States of America'
            self.data.append(policyData)
            policyData = {}

        # fourth table is Bicycle Rental Programs in USA
        policyData = {}
        for row in tables[3].findAll('tr'):
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs).get('href', '')
            policyData['policy_name'] = tags[3].text
            policyData['type'] = 'Bicycle Rental Programs'
            policyData['country'] = 'United States of America'
            self.data.append(policyData)
            policyData = {}

class CarSharing(PageParser):
    '''
    >>> parser = CarSharing()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''                                        
    url = 'http://www.aashe.org/resources/carsharing-campus'
    login_required = True

    def parsePage(self):
        headers = self.soup.find('div', {'class': 'content clear-block'}).findAll('h2')
        policyData = {}
        for header in headers:
            para = header.nextSibling.nextSibling
            elements = [el for el in para]
            for el in elements:
                tag = getattr(el, 'name', None)
                if tag == 'br':
                    policyData['partner'] = header.text
                    self.data.append(policyData)
                    policyData = {}
                    continue
                elif tag == 'a':
                    linkText = el.text
                    url = dict(el.attrs).get('href', '')
                    policyData.update({'url': url, 'institution': linkText})
                elif isinstance(el, NavigableString) and '(article)' not in el.title().lower():
                    institution = el.title().rsplit('-', 1)[0].strip()
                    policyData['institution'] = institution
                # special case for single-node paras
                if len(elements) == 1:
                    policyData['partner'] = header.text
                    self.data.append(policyData)
                    policyData = {}

class BuildingEnergyDashboard(PageParser):
    '''
    >>> parser=BuildingEnergyDashboard()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-building-energy-dashboards'
    login_required = True

    def parsePage(self):
        headers = self.soup.find('div', {'class': 'content clear-block'}).findAll('h2')
        data = {}
        for header in headers:
            row_tags = header.nextSibling.nextSibling.findAll('tr')
            for row in row_tags:
                tags = [el for el in row]
                data['manufacturer_type'] = header.text
                data['institution'] = tags[1].text
                data['url'] = dict(tags[3].first().attrs).get('href', '')
                data['title'] = tags[3].text
                self.data.append(data)
                data = {}
        
class BicyclePlans(SimpleTableParser):
    '''
    >>> parser = BicyclePlans()
    >>> parser.parsePage()
    ...
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-bicycle-plans'
    login_required = True

    def parsePage(self):
        super(BicyclePlans, self).parsePage(headings=False)
        
class BiodieselFleet(PageParser):
    '''
    >>> parser=BiodieselFleet()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/biodiesel-campus-fleets'
    login_required = True

    def processTable(self, table, diesel_type, country, headings=True):
        # get all <tr> tags from the table...
        rows = row_tags = table.findAll('tr')
        policyData = {}
        # loop over each <tr> row and extract the content...
        if headings:
            rows = row_tags[1:]
        for row in rows:
            # get all the <td> tags in the <tr>...
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[5].first().attrs)['href']
            policyData['title'] = tags[5].text
            policyData['country'] = country
            policyData['biodiesel_source'] = diesel_type
            policyData['biodiesel_type'] = tags[3].text
            self.data.append(policyData)
            policyData = {}    

    def parsePage(self):
        data = {}
        countries = headers = self.soup.find('div', {'class': 'content clear-block'}).findAll('h3')
        for country in countries:
            header = country.findPreviousSibling('h2')
            table = country.nextSibling.nextSibling
            self.processTable(table, header.text, country.text, headings=False)

class ElectricVehicleFleet(PageParser):
    '''
    >>> parser=ElectricVehicleFleet()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-electric-vehicle-fleets'
    login_required = True

    def processTable(self, table, country, headings=True):
        # get all <tr> tags from the table...
        rows = row_tags = table.findAll('tr')
        policyData = {}
        # loop over each <tr> row and extract the content...
        if headings:
            rows = row_tags[1:]
        for row in rows:
            # get all the <td> tags in the <tr>...
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['vehicles'] = tags[3].text
            policyData['url'] = dict(tags[5].first().attrs).get('href', '')
            policyData['source_type'] = tags[5].text
            policyData['title'] = policyData['institution']
            policyData['country'] = country
            self.data.append(policyData)
            policyData = {}        

    def parsePage(self):
        headers = self.soup.find('div', {'class': 'content clear-block'}).findAll('h3')
        for country in headers:
            table = country.nextSibling.nextSibling
            self.processTable(table, country.text)
            
class HybridVehicles(PageParser):
    '''
    >>> parser=HybridVehicles()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-hybrid-vehicle-fleets'
    login_required = True

    def processTable(self, table, country, headings=True):
        # get all <tr> tags from the table...
        rows = row_tags = table.findAll('tr')
        policyData = {}
        # loop over each <tr> row and extract the content...
        if headings:
            rows = row_tags[1:]
        for row in rows:
            # get all the <td> tags in the <tr>...
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['vehicles'] = tags[3].text
            policyData['url'] = dict(tags[5].first().attrs)['href']
            policyData['source'] = tags[5].text
            policyData['title'] = policyData['institution']
            policyData['country'] = country
            self.data.append(policyData)
            policyData = {}            

    def parsePage(self):
        headers = self.soup.find('div', {'class': 'content clear-block'}).findAll('h2')
        for country in headers:
            table = country.nextSibling.nextSibling
            self.processTable(table, country.text)
        
class CarBan(SimpleTableParser):
    '''
    >>> parser=CarBan()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-car-bans'
    login_required = True

    def parsePage(self):
        tables = self.soup.findAll('table')
        data = {}
        for table in tables:
            for row in table.findAll('tr')[1:]:
                tags = [el for el in row]
                data['institution'] = tags[1].text
                data['url'] = dict(tags[3].first().attrs).get('href', '')
                data['title'] = tags[3].text
                data['type'] = table.findPreviousSibling('h2').text
                self.data.append(data)
                data = {}                    

class CampusEnergyPlan(PageParser):
    '''
    >>> parser=CampusEnergyPlan()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-energy-plans'
    login_required = True

    def parsePage(self):
        table = self.soup.findAll('table')[0]
        data = {}
        for row in table.findAll('tr')[1:]:
            tags = [el for el in row]
            data['institution'] = tags[1].text
            data['title'] = tags[3].text
            data['url'] = dict(tags[3].find('a').attrs).get('href','')
            data['date_published'] = tags[5].text
            self.data.append(data)
            data = {}

class CampusEnergyWebsite(SimpleTableParser):
    '''
    >>> parser=CampusEnergyWebsite()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-energy-websites'
    login_required = True

class GHGInventory(PageParser):
    '''
    >>> parser = GHGInventory()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-greenhouse-gas-emissions-inventories'

    def parsePage(self):
        tables = self.soup.findAll('table')
        data = {}
        for table in tables:
            for row in table.findAll('tr')[1:]:
                calculator = table.findPreviousSibling('h2')
                tags = [el for el in row]
                data['institution'] = tags[1].text
                data['title'] = tags[3].text
                data['url'] = dict(tags[3].find('a').attrs).get('href','')
                data['calculator'] = calculator
                self.data.append(data)
                data = {} 
        
class WaterConservation(PageParser):
    '''
    >>> parser=WaterConservation()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-water-conservation-efforts'
    login_required = True

    def parsePage(self):
        tables = self.soup.findAll('table')
        data = {}
        for table in tables:
            for row in table.findAll('tr'):
                tags = [el for el in row]
                data['institution'] = tags[1].text
                data['url'] = dict(tags[3].first().attrs).get('href','')
                data['title'] = tags[3].text
                data['country'] = table.findPreviousSibling('h2')
                self.data.append(data)
                data={}

class WindTurbine(PageParser):
    '''
    >>> parser=WindTurbine()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/wind-power-campus-1'
    login_required = False

    def parsePage(self):
        table = self.soup.find('table')
        data = {}
        for row in table.findAll('tr')[1:]:
            tags = [el for el in row]
            data['institution'] = tags[1].text
            data['capacity'] = tags[3].text
            data['url'] = dict(tags[5].first().attrs).get('href','')
            others = [anchor['href'] for anchor in tags[5].findAll('a')[1:]]
            data['other_urls'] = ' '.join(others)
            self.data.append(data)
            data={}
    
class GenericGreenBuilding(PageParser):
    para_skip = 4
    login_required = True

    def getParas(self):
        return self.soup.find('div', {'class': 'content clear-block'}).findAll('p')[self.para_skip:]

    def getParagraphTags(self, paragraph):
        return [el for el in paragraph]

    def getTagElements(self, tag):
        return [el for el in tag]
    
    def parsePage(self):
        # skip first `para_skip` paragraphs
        paras = self.getParas()
        data = {}
        for para in paras:
            tags = self.getParagraphTags(para)
            #tags = [el for el in para]
            els = self.getTagElements(tags[0])
            #els = [el for el in tags[1]]
            inst = els[0]
            data['institution'] = inst.strip()
            try:
                facility = els[2]
                data['facility_name'] = facility.strip()
            except:
                data['facility_name'] = ''
            try:
                year = tags[4] or ''
                data['year'] = year.strip()
            except:
                data['year'] = ''
            try:
                sqft = tags[8] or ''
                data['sqft'] = sqft.strip()
            except:
                data['sqft'] = ''
            try:
                cost = tags[12] or ''
                data['cost'] = cost.strip()
            except:
                data['cost'] = ''
            try:
                cert = tags[16] or ''
                data['certification'] = cert.strip()
            except:
                data['certification'] = ''
            try:
                key_feat = tags[20] or ''
                data['key_features'] = key_feat.strip()
            except:
                data['key_features'] = ''
            try:
                anchor = tags[26]
                if isinstance(anchor, NavigableString):
                    data['url'] = ''
                    data['title'] = data['institution'] + data['year']
                else:
                    data['url'] = dict(tags[26].attrs).get('href', '')
                    data['title'] = tags[26].text
            except:
                data['url'] = ''
                data['title'] = data['institution'] + data['year']
            self.data.append(data)
            data = {}

class GreenAthleticBuilding(GenericGreenBuilding):
    '''
    >>> parser=GreenAthleticBuilding()
    >>> paras = parser.getParas()
    >>> tags = parser.getParagraphTags(paras[0])
    >>> len(tags) > 0
    True
    >>> els = parser.getTagElements(tags[0])
    >>> len(els) > 0
    True
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/athletic-recreation-centers-stadiums'
    para_skip = 4

class GreenLibrary(GenericGreenBuilding):
    '''
    >>> parser=GreenLibrary()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/green-libraries-campus'
    para_skip = 4

class GreenStudentCenter(GenericGreenBuilding):
    '''
    >>> parser = GreenStudentCenter()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/green-student-centers'
    para_skip = 4

class GreenResidence(GenericGreenBuilding):
    '''
    >>> parser = GreenResidence()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/green-residence-halls'
    para_skip = 4

    def parsePage(self):
        paras = self.getParas()
        data = {}
        for para in paras:
            #tags = [el for el in para]
            tags = self.getParagraphTags(para)
            #els = [el for el in tags[1]]
            els = self.getTagElements(tags[0])
            inst = els[0]
            data['institution'] = inst.strip()
            try:
                facility = els[2]
                data['facility_name'] = facility.strip()
            except:
                data['facility_name'] = ''
            try:
                year = tags[4] or ''
                data['year'] = year.strip()
            except:
                data['year'] = ''
            try:
                sqft = tags[8] or ''
                data['sqft'] = sqft.strip()
            except:
                data['sqft'] = ''
            try:
                cost = tags[12] or ''
                data['cost'] = cost.strip()
            except:
                data['cost'] = ''
            try:
                beds = tags[16] or ''
                data['beds'] = beds.strip()
            except:
                data['beds'] = ''
            try:
                cert = tags[20] or ''
                data['certification'] = cert.strip()
            except:
                data['certification'] = ''
            try:
                key_feat = tags[24] or ''
                data['key_features'] = key_feat.strip()
            except:
                data['key_features'] = ''
            try:
                anchor = tags[30]
                if isinstance(anchor, NavigableString):
                    data['url'] = ''
                    data['title'] = data['institution'] + data['year']
                else:
                    data['url'] = dict(anchor.attrs).get('href', '')
                    data['title'] = anchor.text
            except:
                data['url'] = ''
                data['title'] = data['institution'] + data['year']
            self.data.append(data)
            data = {}
    
class GreenScience(GenericGreenBuilding):
    '''
    >>> parser = GreenScience()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/green-science-buildings'
    para_skip = 4

class RenewableEnergyResearchCenters(SimpleTableParser):
    '''
    >>> parser=RenewableEnergyResearchCenters()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/renewable-energy-research-centers'
    login_required = True

class FuelCells(SimpleTableParser):
    '''
    >>> parser = FuelCells()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-installations-stationary-fuel-cells'
    login_required = True

    def processTableData(self, row, tags):
        policyData = {}
        policyData['institution'] = tags[1].text
        policyData['url'] = dict(tags[5].first().attrs)['href']
        policyData['title'] = policyData['institution']
        policyData['capacity'] = tags[3].text
        return policyData

class SustainableLandscaping(SimpleTableParser):
    '''
    >>> parser = SustainableLandscaping()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/sustainable-landscaping-campus'
    login_required = True

class WebsiteCampusGreenBuilding(PageParser):
    '''
    >>> parser = WebsiteCampusGreenBuilding()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/websites-campus-green-building'
    login_required = True

    def parsePage(self):
        ulist = self.soup.find('div', {'class': 'content clear-block'}).find('ul')
        data = {}
        for li in ulist.findAll('li'):
            anchor = li.find('a')
            br = li.find('br')
            text = br.nextSibling
            data['institution'] = ''
            data['title'] = anchor.text
            data['url'] = dict(anchor.attrs).get('href','')
            data['description'] = text
            self.data.append(data)
            data = {}

