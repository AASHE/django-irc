from base import PageParser, SimpleTableParser
from BeautifulSoup import BeautifulSoup, NavigableString


class CampusAgriculture(SimpleTableParser):
    '''
    >>> parser = CampusAgriculture()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-supported-agriculture-and-farms'
    login_required = True

    def process_table(self, table, country):
        # get all <tr> tags from the table...
        row_tags = table.findAll('tr')
        policyData = {}
        # loop over each <tr> row and extract the content...
        for row in row_tags[1:]:
            # get all the <td> tags in the <tr>...
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs)['href']
            policyData['title'] = tags[3].text
            policyData['country'] = country
            self.data.append(policyData)
            policyData = {}        

    def parsePage(self):
        # first table on page is Canada, second is USA
        canada_table = self.soup.findAll('table')[0]
        us_table = self.soup.findAll('table')[1]
        self.process_table(canada_table, 'Canada')
        self.process_table(us_table, 'United States of America')

class SustainableLivingGuide(PageParser):
    '''
    >>> parser = SustainableLivingGuide()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-sustainable-living-guides'
    login_required = True

    def parsePara(self, para):
        policyData = {}
        for el in para:
            tag = getattr(el, 'name', None)
            if tag == 'br':
                self.data.append(policyData)
                policyData = {}
                continue
            elif tag == 'a':
                linkText = el.text
                url = dict(el.attrs).get('href', None)
                policyData.update({'url': url, 'policy_name': linkText})
            elif isinstance(el, NavigableString) and '(pdf)' not in el.title().lower():
                institution = el.title().rsplit('-', 1)[0].strip()
                policyData['institution'] = institution
    
    def parsePage(self):
        # parse the first paragraph (Canada)
        self.parsePara(self.soup.findAll('p')[0])
        # parse the second paragraph (USA)
        self.parsePara(self.soup.findAll('p')[1])        

class SustainabilityLivingGuide(PageParser):
    '''
    >>> parser = SustainabilityLivingGuide()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-sustainable-living-guides'
    login_required = True

    def parsePage(self):
        paras = self.soup.findAll('p')
        guideData = {}
        canada, usa = 0, 1
        canada_nodes = [el for el in paras[canada]]
        usa_nodes = [el for el in paras[usa]]        
        for el in canada_nodes:
            tag = getattr(el, 'name', None)
            if tag == 'br':
                self.data.append(guideData)
                guideData = {}
                continue            
            elif tag == 'a':
                linkText = el.text
                url = dict(el.attrs).get('href', None)
                guideData.update({'url': url, 'title': linkText})
            elif isinstance(el, NavigableString):
                institution = el.title().rsplit('-', 1)[0].strip()
                guideData['institution'] = institution

        for el in usa_nodes:
            tag = getattr(el, 'name', None)
            if tag == 'br':
                self.data.append(guideData)
                guideData = {}
                continue
            elif tag == 'a':
                linkText = el.text
                url = dict(el.attrs).get('href', None)
                guideData.update({'url': url, 'title': linkText})
            elif isinstance(el, NavigableString) and '(pdf)' not in el.title().lower():
                institution = el.title().rsplit('-', 1)[0].strip()
                guideData['institution'] = institution

class CampusGardens(SimpleTableParser):
    '''
    >>> parser = CampusGardens()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-and-campus-community-gardens'
    login_required = True

    def processTableData(self, row, tags):
        policyData = {}
        policyData['institution'] = tags[1].text
        try:
            policyData['url'] = dict(tags[5].first().attrs).get('href', '')
        except:
            policyData['url'] = ''            
        policyData['title'] = policyData['institution']
        policyData['country'] = row.findPrevious('h3').text
        return policyData
                
class AcademicCentersParser(PageParser):
    login_required = True

    def processTable(self, table):
        # get all <tr> tags from the table...
        row_tags = table.findAll('tr')
        policyData = {}
        # loop over each <tr> row and extract the content...
        for row in row_tags[1:]:
            # get all the <td> tags in the <tr>...
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs)['href']
            policyData['name_of_center'] = tags[3].text
            policyData['category'] = self.category            
            self.data.append(policyData)
            policyData = {}
    
    def parsePage(self):
        # data is in the first <table> on the page
        self.processTable(self.soup.findAll('table')[0])    

class AcademicCentersAgriculture(AcademicCentersParser):
    url = 'http://www.aashe.org/resources/academic-centers-and-research-initiatives-sustainable-agriculture'
    category = 'AG'
    
class AcademicCentersArchitecture(AcademicCentersParser):
    url = 'http://www.aashe.org/resources/design_centers.php'
    category = 'AR'
    
class AcademicCentersBusiness(AcademicCentersParser):
    url = 'http://www.aashe.org/resources/business_centers.php'
    category = 'BS'
    
class AcademicCentersDevelopmentStudies(AcademicCentersParser):
    url = 'http://www.aashe.org/resources/sustainable_development_centers.php'
    category = 'DS'
    
class AcademicCentersEconomics(AcademicCentersParser):
    url = 'http://www.aashe.org/resources/economics_centers.php'
    category = 'EC'
    
class AcademicCentersEducation(AcademicCentersParser):
    url = 'http://www.aashe.org/resources/education_centers.php'
    category = 'ED'
    
class AcademicCentersEngineering(AcademicCentersParser):
    url = 'http://www.aashe.org/resources/engineeringcenters.php'
    category = 'EN'
    
class AcademicCentersLaw(AcademicCentersParser):
    url = 'http://www.aashe.org/resources/law_centers.php'
    category = 'LW'

class AcademicCentersUrbanStudies(AcademicCentersParser):
    url = 'http://www.aashe.org/resources/urban_studies_centers.php'
    category = 'US'

class SustainabilityResearchInventories(SimpleTableParser):
    url = 'http://www.aashe.org/resources/sustainability-research-inventories'
    login_required = True

# TODO
class CoursesOnSustainability(PageParser):
    url = 'http://www.aashe.org/resources/courses-campus-sustainability'
    login_required = False

class SustainableCourseInventories(SimpleTableParser):
    '''
    >>> parser = SustainableCourseInventories()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/sustainability-course-inventories'
    login_required = True

class SustainabilitySyllabi(PageParser):
    '''
    >>> parser = SustainabilitySyllabi()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/sustainability-related-syllabi-databases'
    login_required = True

    def parsePage(self):
        paras = self.soup.findAll('p')[1:-6]
        syllabiData = {}
        for p in paras:
            nodes = [el for el in p]
            syllabiData['syllabi_name'] = nodes[3].text
            syllabiData['organization'] = nodes[0].text
            syllabiData['url'] = dict(nodes[3].attrs).get('href', '')
            syllabiData['description'] = nodes[5].title()
            self.data.append(syllabiData)
            syllabiData = {}

class FacultyDevelopmentWorkshops(SimpleTableParser):
    '''
    >>> parser = FacultyDevelopmentWorkshops()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/sustainability-faculty-development-workshops'
    login_required = True
            
class SurveysAwarenessAttitudes(SimpleTableParser):
    '''
    >>> parser = SurveysAwarenessAttitudes()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/surveys-sustainability-awareness-attitudes-and-values'
    login_required = True
