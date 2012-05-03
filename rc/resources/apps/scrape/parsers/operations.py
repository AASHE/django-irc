import calendar
from datetime import datetime

from BeautifulSoup import BeautifulSoup, NavigableString, Tag
import requests
from StringIO import StringIO
import pyPdf

from base import ElectronicWasteParser, PageParser, SimpleTableParser

BASE_URL = 'http://www.aashe.org/resources/'

def get_url_title(url):
    """Try to load url and return a tuple of its title and any
    error text.

    Works for html and pdf (but not, e.g., Word docs).
    """
    notes = ''
    try:
        page = requests.get(url)
    except Exception as ex:
        title = 'Source'
        notes = 'Error loading url: "{}".'.format(str(ex))
    else:
        # Test page.url rather than url parameter since redirection
        # can route to something other than the url parameter.
        if not page.url.endswith('pdf'):
            try:
                soup = BeautifulSoup(
                    page.text, convertEntities=BeautifulSoup.HTML_ENTITIES)
                title = soup.find('head').find('title').text
            except Exception as ex:
                title = 'Source'
                notes = 'Error parsing page: "{}".'.format(str(ex))
        else:
            try:
                pdf = pyPdf.PdfFileReader(StringIO(page.content))
                title = pdf.documentInfo['/Title']
            except Exception as ex:
                title = 'Source'
                notes = 'Error parsing PDF: "{}".'.format(str(ex))
    if not title.strip():
        title = 'Source'
    return title, notes


class BottledWaterBans(PageParser):
    '''
    >>> parser = BottledWaterBans()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'bottled-water-elimination-and-reduction'
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
    url = BASE_URL + 'sustainable-dining-initiatives-campus'
    login_required = True

    def parsePage(self):
        headers = self.soup.find('div',
                                 {'class': 'content clear-block'}).findAll('h2')
        for header in headers:
            para = header.findNextSibling('p')
            anchors = para.findAll('a')
            for anchor in anchors:
                self.data.append(
                    {'type': header.text,
                     'url': anchor['href'],
                     'title': anchor.text,
                     'institution': anchor.previousSibling.strip(' - ')})

class SustainabilityPurchasing(PageParser):
    '''
    >>> parser = SustainabilityPurchasing()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'links-related-sustainable-purchasing-campus'
    login_required = True

    def parsePage(self):
        headers = self.soup.find('div', {'class':
                                         'content clear-block'}).findAll('h2')
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
                    policyData.update({'url': url, 'title': linkText})
                elif (isinstance(el, NavigableString) and
                      '(article)' not in el.title().lower() and
                      '**' not in el.title().lower()):
                    institution = el.title().rsplit('-', 1)[0].strip()
                    policyData['institution'] = institution

class AlternativeTransport(PageParser):
    '''
    >>> parser = AlternativeTransport()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-alternative-transportation-websites'
    login_required = True

    def parsePage(self):
        paragraph = self.soup.find(
            'div', {'class': 'content clear-block'}).findAll('p')[1]
        for anchor in paragraph.findAll('a'):
            try:
                institution = anchor.previousSibling.extract().strip('\n -')
                if (anchor.nextSibling and
                    not isinstance(anchor.nextSibling, Tag)):
                    notes = anchor.nextSibling.extract()
                else:
                    notes = ''
                anchor = anchor.extract()
                url = anchor['href']
                title = anchor.text
                self.data.append({'institution': institution,
                                  'title': title,
                                  'url': url,
                                  'notes': notes})
            except Exception as e:
                print 'exception {0} rasied for for anchor: {0}'.format(
                    e, anchor)

class UniversalAccess(SimpleTableParser):
    '''
    >>> parser = UniversalAccess()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-universal-transit-passes'
    login_required = False

    def parsePage(self):
        tables = self.soup.findAll('table')
        for table in tables[0:2]:
            self.processTable(table=table,
                              pass_type='Universal Bus/Transit Pass Programs')
        for table in tables[2:]:
            self.processTable(table=table,
                              pass_type='Bus/Transit Pass Discount Programs')

    def processTable(self, table, pass_type):
        transit_passes = super(UniversalAccess, self).processTable(
            table=table, headings=False, save_resources=False)
        for transit_pass in transit_passes:
            transit_pass['type'] = pass_type
        self.data.extend(transit_passes)
        return transit_passes

class CarSharing(PageParser):
    '''
    >>> parser = CarSharing()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'carsharing-campus'
    login_required = True

    def parsePage(self):
        headers = self.soup.find('div', {'class':
                                         'content clear-block'}).findAll('h2')
        for header in headers:
            para = header.findNextSibling('p')
            for anchor in para.findAll('a'):
                self.data.append({'partner': header.text,
                                  'url': anchor['href'],
                                  'institution': anchor.text})

class BuildingEnergyDashboard(SimpleTableParser):
    '''
    >>> parser=BuildingEnergyDashboard()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-building-energy-dashboards'
    login_required = True

    def parsePage(self):
        content_div = self.soup.find(
            'div', {'class': 'content clear-block'})
        for table in content_div.findAll('table'):
            dashboards = self.processTable(table=table, headings=False,
                                           save_resources=False)
            manufacturer_type = table.findPrevious('h2').text
            for dashboard in dashboards:
                dashboard['manufacturer_type'] = manufacturer_type
            self.data.extend(dashboards)

class BicyclePlans(SimpleTableParser):
    '''
    >>> parser = BicyclePlans()
    >>> parser.parsePage()
    ...
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-bicycle-plans'
    login_required = True

    def parsePage(self):
        super(BicyclePlans, self).parsePage(headings=False)

class BiodieselFleet(SimpleTableParser):
    '''
    >>> parser=BiodieselFleet()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'biodiesel-campus-fleets'
    login_required = True

    def processTableData(self, row):
        fleets = super(BiodieselFleet, self).processTableData(
            row=row, anchor_cell_num=2)
        production_type = row.findPrevious('h2').text
        cells = row.findAll('td')
        for fleet in fleets:
            fleet['type'] = cells[1].text
            fleet['production'] = production_type
        return fleets

    def parsePage(self):
        content_div = self.soup.find('div',
                                     {'class': 'content clear-block'})
        for table in content_div.findAll('table'):
            self.processTable(table=table, headings=False)

class ElectricVehicleFleet(SimpleTableParser):
    '''
    >>> parser=ElectricVehicleFleet()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-electric-vehicle-fleets'
    login_required = True

    def processTableData(self, row):
        resources = super(ElectricVehicleFleet, self).processTableData(
            row=row, anchor_cell_num=2)
        cells = row.findAll('td')
        for resource in resources:
            resource['number'] = cells[1].text
            resource['title'], _ = get_url_title(resource['url'])
        return resources

    def parsePage(self):
        content_div = self.soup.find('div',
                                     {'class': 'content clear-block'})
        for table in content_div.findAll('table'):
            self.processTable(table=table, headings=True)

class HybridVehicles(SimpleTableParser):
    '''
    >>> parser=HybridVehicles()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-hybrid-vehicle-fleets'
    login_required = True

    def processTableData(self, row):
        fleets = super(HybridVehicles, self).processTableData(row=row,
                                                              anchor_cell_num=2)
        cells = row.findAll('td')
        for fleet in fleets:
            fleet['number'] = cells[1].text
        return fleets

    def parsePage(self):
        content_div = self.soup.find('div',
                                     {'class': 'content clear-block'})
        for table in content_div.findAll('table'):
            self.processTable(table=table, headings=True)

class CarBan(SimpleTableParser):
    '''
    >>> parser=CarBan()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-car-bans'
    login_required = True

    def parsePage(self):
        tables = self.soup.findAll('table')
        for table in tables:
            bans = self.processTable(table=table, save_resources=False)
            ban_type = table.findPreviousSibling('h2').text
            for ban in bans:
                ban['type'] = ban_type
            self.data.extend(bans)

class CampusEnergyPlan(PageParser):
    '''
    >>> parser=CampusEnergyPlan()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-energy-plans'
    login_required = True

    def parsePage(self):
        table = self.soup.findAll('table')[0]
        data = {}
        for row in table.findAll('tr')[1:]:
            tags = [el for el in row]
            data['institution'] = tags[1].text
            data['title'] = tags[3].text
            data['url'] = dict(tags[3].find('a').attrs).get('href','')
            try:
                month, year = tags[5].text.split('/')
                dt = datetime(month=int(month), year=2000 + int(year), day=1)
                data['date_published'] = dt
            except:
                data['date_published'] = None
            self.data.append(data)
            data = {}

class CampusEnergyWebsite(SimpleTableParser):
    '''
    >>> parser=CampusEnergyWebsite()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-energy-websites'
    login_required = True

class GHGInventory(PageParser):
    '''
    >>> parser = GHGInventory()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-greenhouse-gas-emissions-inventories'

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

class WaterConservation(SimpleTableParser):
    '''
    >>> parser = WaterConservation()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-water-conservation-efforts'
    login_required = True

    def parsePage(self):
        for table in self.soup.findAll('table'):
            self.processTable(table=table, headings=False)

class WindTurbine(SimpleTableParser):
    '''
    >>> parser=WindTurbine()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'wind-power-campus-1'
    login_required = False

    def parsePage(self):
        for table in self.soup.findAll('table'):
            self.processTable(table=table, headings=True)

    def processTableData(self, row):
        resources = super(WindTurbine, self).processTableData(row=row,
                                                              anchor_cell_num=2)
        cells = row.findAll('td')
        for resource in resources:
            resource['size'] = cells[1].text
            resource['title'], _ = get_url_title(resource['url'])
        return resources

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
            data['type'] = self.soup.find('h1', {'class': 'page-title'}).text
            self.data.append(data)
            data = {}

class GreenAthleticBuilding(GenericGreenBuilding):
    '''
    >>> parser = GreenAthleticBuilding()
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
    url = BASE_URL + 'athletic-recreation-centers-stadiums'
    para_skip = 4

class GreenLibrary(GenericGreenBuilding):
    '''
    >>> parser = GreenLibrary()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'green-libraries-campus'
    para_skip = 4

class GreenStudentCenter(GenericGreenBuilding):
    '''
    >>> parser = GreenStudentCenter()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'green-student-centers'
    para_skip = 4

class GreenResidence(GenericGreenBuilding):
    '''
    >>> parser = GreenResidence()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'green-residence-halls'
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
            data['type'] = self.soup.find('h1', {'class': 'page-title'}).text
            self.data.append(data)
            data = {}

class GreenScience(GenericGreenBuilding):
    '''
    >>> parser = GreenScience()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'green-science-buildings'
    para_skip = 4

class RenewableEnergyResearchCenters(SimpleTableParser):
    '''
    >>> parser = RenewableEnergyResearchCenters()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'renewable-energy-research-centers'
    login_required = True

class FuelCells(SimpleTableParser):
    '''
    >>> parser = FuelCells()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-installations-stationary-fuel-cells'
    login_required = True

    def processTableData(self, row):
        fuel_cells = super(FuelCells, self).processTableData(
            row=row, anchor_cell_num=2)
        size = row.findAll('td')[1].text
        for fuel_cell in fuel_cells:
            fuel_cell['size'] = size
            fuel_cell['title'], _ = get_url_title(fuel_cell['url'])
        return fuel_cells

class SustainableLandscaping(SimpleTableParser):
    '''
    >>> parser = SustainableLandscaping()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'sustainable-landscaping-campus'
    login_required = True

class WebsiteCampusGreenBuilding(PageParser):
    '''
    >>> parser = WebsiteCampusGreenBuilding()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'websites-campus-green-building'
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

class GlobalWarmingCommitment(SimpleTableParser):
    '''
    >>> parser = GlobalWarmingCommitment()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-global-warming-commitments'
    login_required = True

    def processTableData(self, row):
        commitments = super(GlobalWarmingCommitment, self).processTableData(row)
        cells = row.findAll('td')
        date_string = cells[-1].text
        try:
            month = date_string.split()[0]
            year = date_string.split()[-1]
            month_num = list(calendar.month_abbr).index(month[0:3])
            commitment_date = datetime(month=month_num, year=int(year),
                                       day=1)
        except:
            commitment_date = None
        for commitment in commitments:
            # GlobalWarmingCommitments have a commitment field where
            # other resource items have a title.
            commitment['commitment'] = commitment.pop('title')
            if commitment_date:
                commitment['date'] = commitment_date
            else:
                commitment['notes'] = ('unparsed commitment date: ' +
                                       date_string)
        return commitments

class CommuterSurvey(SimpleTableParser):
    '''
    >>> parser = CommuterSurvey()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-commuter-surveys'
    login_required = True

    def processTable(self, table, surveytype):
        surveys = super(CommuterSurvey, self).processTable(
            table=table, save_resources=False)
        for survey in surveys:
            survey['type'] = surveytype
        self.data.extend(surveys)

    def parsePage(self):
        headers = self.soup.find('div',
                                 {'class': 'content clear-block'}).findAll('h2')
        for surveytype in headers:
            table = surveytype.nextSibling.nextSibling
            self.processTable(table, surveytype.text)

class ElectronicWasteEvents(ElectronicWasteParser):

    def parsePage(self):
        super(ElectronicWasteEvents, self).parsePage('events')

class RecyclingWasteMinimization(SimpleTableParser):
    '''
    >>> parser = RecyclingWasteMinimization()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-recycling-and-waste-minimization-websites'
    login_required = True
