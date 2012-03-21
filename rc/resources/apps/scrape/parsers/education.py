'''Parsers for education resources.'''
import copy
import urllib

from BeautifulSoup import BeautifulSoup, NavigableString, Tag

from base import PageParser, SimpleTableParser


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

    def parsePage(self, headings=True, debug=False):
        if debug:
            import pdb; pdb.set_trace()
        for table in self.soup.findAll('table'):
            self.processTable(table, headings=headings)

    def processTableData(self, row, tags):
        # get rid of bothersome NavigableStrings:
        tags = [ t for t in tags if isinstance(t, Tag) ]
        gardenData = {}
        gardenData['institution'] = tags[0].text
        gardenLink = tags[-1].find('a').extract()
        gardenData['url'] = gardenLink['href']
        gardenData['title'] = gardenLink.text
        # sometimes there's a bit of text after the link -- this goes
        # in the notes field:
        if tags[-1].text:
            gardenData['notes'] = 'text after link: {0}'.format(tags[-1].text)
        return gardenData
                
class AcademicCentersParser(PageParser):
    '''Base parser for Academic Centers resources.

    Subclass for each type of Academic Center, and provide values
    for url and category.
    '''
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
    '''
    >>> parser = AcademicCentersAgriculture()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/academic-centers-and-research-initiatives-sustainable-agriculture'
    category = 'AG'
    
class AcademicCentersArchitecture(AcademicCentersParser):
    '''
    >>> parser = AcademicCentersArchitecture()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/design_centers.php'
    category = 'AR'
    
class AcademicCentersBusiness(AcademicCentersParser):
    '''
    >>> parser = AcademicCentersBusiness()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/business_centers.php'
    category = 'BS'
    
class AcademicCentersDevelopmentStudies(AcademicCentersParser):
    '''
    >>> parser = 
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/sustainable_development_centers.php'
    category = 'DS'
    
class AcademicCentersEconomics(AcademicCentersParser):
    '''
    >>> parser = AcademicCentersEconomics()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/economics_centers.php'
    category = 'EC'
    
class AcademicCentersEducation(AcademicCentersParser):
    '''
    >>> parser = AcademicCentersEducation()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/education_centers.php'
    category = 'ED'
    
class AcademicCentersEngineering(AcademicCentersParser):
    '''
    >>> parser = AcademicCentersEngineering()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/engineeringcenters.php'
    category = 'EN'
    
class AcademicCentersLaw(AcademicCentersParser):
    '''
    >>> parser = AcademicCentersLaw()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/law_centers.php'
    category = 'LW'

class AcademicCentersUrbanStudies(AcademicCentersParser):
    '''
    >>> parser = AcademicCentersUrbanStudies()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/urban_studies_centers.php'
    category = 'US'

class SustainabilityResearchInventories(SimpleTableParser):
    url = 'http://www.aashe.org/resources/sustainability-research-inventories'
    login_required = True

class CampusSustainabilityCourses(PageParser):
    '''
    >>> parser = CoursesOnSustainability()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/courses-campus-sustainability'
    login_required = False

    def allCourseElementsForTitleElement(self, title_element):
        '''Parses titles out of title_element, and returns a list
        of elements representing courses for each title.

        Needed for cases where two courses are listed with the same
        teachers and description.  E.g. Aquinas College courses.
        '''
        course_elements = list()
        titles = [ t for t in title_element.contents 
                   if t.string  and t.string.strip() ]
        if len(titles) > 1:
            # need to return a number of title elements, each
            # associated with the same teachers and description.
            for title in titles:
                # duplicate title_element replacing the actual
                # title text with this title
                assert title_element.parent is title_element.findPrevious()
                new_course_element = copy.deepcopy(
                    self.courseElementForTitleElement(title_element))
                new_title_element = self.titleElement(new_course_element)
                new_title_element.setString(title)
                course_elements.append(new_course_element)
        else:
            course_elements.append(
                self.courseElementForTitleElement(title_element))
        return course_elements

    def courseElementForTitleElement(self, title_element):
        '''Given a title_element, return the corresponding course element.
        '''
        return title_element.findPrevious('p')
    
    def parseCourse(self, element):
        '''Parse course info from element.'''
        course = dict()
        title_element = element.find('strong')
        course['title'] = self.titleElement(element).text.strip()
        # sometimes there's a link in the title:
        if title_element.find('a'):
            course['url'] = title_element.find('a').get('href')
        # sometimes the title is wrapped in an anchor tag:
        elif title_element.parent.name == 'a':
            course['url'] = title_element.parent.get('href')
        course['teachers'] = self.parseTeachers(element, course)
        course['description'] = self.parseDescription(element)
        return course

    def parseDescription(self, course_element):
        '''Pull the description out of a course element.

        Description is the last bits of course_element.  These can be
        strings, or BeautifulSoup tags.
        '''
        em_index = course_element.index(course_element.findAll('em')[-1])
        description = ''
        for part in course_element.contents[em_index + 1:]:
            # skip BR tags:
            try:
                if part.name.lower() == 'br':
                    continue
            except AttributeError:
                pass  # not a BeautifulSoup.Tag
            description = ''.join((description, str(part).strip()))
        return description
    
    def parseTeacher(self, anchor, text):
        '''Return a dict of teacher info parsed from an anchor tag and a
        string.'''
        if not text:  # some data is unexpectedly formatted or missing
            return 

        # initialize teacher fields that might not be present so they'll
        # exist when the loader tries to access them:
        teacher = dict(email='', web_page='', middle_name='',
                       title='', department='')
        
        protocol, resource = anchor['href'].split(':')
        if protocol.lower() == 'mailto':
            teacher['email'] = urllib.unquote(resource).strip()
        elif protocol.lower() == 'http':
            teacher['web_page'] = ':'.join((protocol, 
                                            urllib.unquote(resource).strip()))

        names = anchor.text.split()
        teacher['first_name'] = names.pop(0)
        teacher['last_name'] = names.pop()
        if names:
            teacher['middle_name'] = names[0]

        if text.startswith(','):
            text = text[1:]
        teacher['title'] = text.strip()

        return teacher
    
    def parseTeachers(self, element, course):
        '''Return a list of teacher info parsed from a course element.

        Teacher info is wrapped in an <em>.  Inside, there's (always?)
        a mailto anchor with email address and name, followed by a
        title and sometimes, a department.  When there are > 1
        teachers, they sometimes are wrapped in individual <em>'s,
        sometimes combined into the same <em>.
        '''
        teachers = list()
        for em in element.findAll('em'):
            for a in em.findAll('a'):
                teacher = self.parseTeacher(a, a.nextSibling)
                if teacher:
                    teachers.append(teacher)
                else:
                    course['notes'] = '\n'.join(
                        (course.setdefault('notes', ''), 
                         "Can't parse a teacher from '{0}'".format(a.parent)))
        return teachers

    def parsePage(self, trace=False):
        '''Parse the page at self.url.

        Call with trace=True for interactive debugging.

        Identifies schools by h2 tags.

        Schools are a dict with a school_name and a list of courses.
        '''
        if trace:
            import pdb; pdb.set_trace()
        for school_element in self.soup.findAll('h2', {'class': None}):
            school = dict(school_name=school_element.text, courses=list())
            next_sibling = school_element.findNextSibling()
            while (next_sibling and 
                   next_sibling.name.lower() == 'p' and
                   next_sibling.text > ''):  # skip empty paragraphs
                # some courses share the same description and teachers,
                # and are listed only once -- so pick the titles apart
                # and add a course for each of them:
                title_element = self.titleElement(next_sibling)
                course_elements = self.allCourseElementsForTitleElement(
                    title_element)
                for course_element in course_elements:
                    course = self.parseCourse(course_element)
                    school['courses'].append(course)
                next_sibling = next_sibling.findNextSibling()
            self.data.append(school)            

    def titleElement(self, course_element):
        '''Return the title element parsed from a course element.'''
        return course_element.find('strong')

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
            syllabiData['institution'] = nodes[0].text
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
