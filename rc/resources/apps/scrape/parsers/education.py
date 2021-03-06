'''Parsers for education resources.'''
import copy
import urllib

from BeautifulSoup import Tag

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

    def parsePage(self, headings=True):
        for table in self.soup.findAll('table'):
            self.processTable(table=table, headings=headings)


class SustainableLivingGuide(PageParser):
    '''
    >>> parser = SustainableLivingGuide()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-sustainable-living-guides'
    login_required = True

    def parseParagraph(self, paragraph):
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

    def parsePage(self):
        content_div = self.soup.find('div', {'class': 'content clear-block'})
        for paragraph in content_div.findAll('p'):
            self.parseParagraph(paragraph)

class CampusGardens(SimpleTableParser):
    '''
    >>> parser = CampusGardens()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-and-campus-community-gardens'
    login_required = True

    def parsePage(self, headings=True):
        for table in self.soup.findAll('table'):
            self.processTable(table, headings=headings)

class AcademicCentersParser(SimpleTableParser):
    '''Base parser for Academic Centers resources.

    Subclass for each type of Academic Center, and provide values
    for url and category.
    '''
    login_required = True

    def processTable(self, table, headings=True):
        super(AcademicCentersParser, self).processTable(table, headings)
        # tuck policy category into each scraped policy
        for policy in self.data:
            policy['category'] = self.category

    def parsePage(self, all_tables=False, headings=True):
        for table in self.soup.findAll('table'):
            self.processTable(table=table, headings=headings)
            if not all_tables:
                return

class AcademicCentersAgriculture(AcademicCentersParser):
    '''
    >>> parser = AcademicCentersAgriculture()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/academic-centers-and-research-initiatives-sustainable-agriculture'
    category = 'AG'

    def parsePage(self):
        super(AcademicCentersAgriculture, self).parsePage(headings=False)

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

    def parsePage(self):
        super(AcademicCentersEconomics, self).parsePage(all_tables=True)

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

    def parsePage(self):
        super(AcademicCentersEngineering, self).parsePage(headings=False)

class AcademicCentersLaw(AcademicCentersParser):
    '''
    >>> parser = AcademicCentersLaw()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/law_centers.php'
    category = 'LW'

    def parsePage(self):
        super(AcademicCentersLaw, self).parsePage(all_tables=True)

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
            description = ' '.join((description, str(part).strip()))
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
        paras = self.soup.findAll('p')[1:-5]
        syllabiData = {}
        for p in paras:
            nodes = [el for el in p]
            link = p.findNext('a')
            syllabiData['url'] = link['href']
            syllabiData['title'] = link.text
            syllabiData['institution'] = nodes[0].text
            syllabiData['description'] = nodes[5].strip()
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

class SustainabilityNetworks(PageParser):
    '''
    >>> parser = AlumniSustainabilityNetworks()
    >>> parser.parsePage()
    >>> len(parser.data) > 0
    True
    '''
    url = 'http://www.aashe.org/resources/alumni-sustainability-networks'

    def parsePage(self):
        content_div = self.soup.find('div', {'class': 'content clear-block'})
        list = content_div.find('ul')
        for li in list.findAll('li'):
            network = dict()
            anchor = li.find('a').extract()
            network['url'] = anchor['href']
            network['title'] = anchor.text.strip()
            # maybe we'll get a lucky match:
            network['institution'] = network['title'].split()[0]
            if li.text:
                network['description'] = li.text
            self.data.append(network)

class SustainabilityMaps(PageParser):
    '''
    >>> parser = AlumniSustainabilityNetworks()
    >>> parser.parsePage()
    >>> len(parser.data) > 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-sustainability-mapstours'

    def parsePage(self):
        content_div = self.soup.find('div', {'class': 'content clear-block'})
        p = content_div.find('p')
        while p.contents:
            map = dict()
            anchor = p.contents.pop()
            map['url'] = anchor['href']
            map['title'] = anchor.text
            map['institution'] = p.contents.pop().strip().strip('-').strip()
            # swallow the <br>:
            if p.contents:  # except for the first resource listed
                p.contents.pop()
            self.data.append(map)

class StudyAbroad(PageParser):
    '''
    >>> parser = StudyAbroad()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/study-abroad-programs-sustainability'
    login_required = False

    def parsePage(self):
        headings = self.soup.findAll('h2', {'class': None})
        for heading in headings:
            if heading.text == 'Institutions Offering Study Abroad Programs in Sustainability':
                program_type = 'IN'
            elif heading.text == 'Organizations Offering Sustainability Study Abroad Programs':
                program_type = 'OT'

            table = heading.findNextSibling()
            rows = table.findAll('tr')
            # skip heading
            for row in rows[1:]:
                program = dict()
                cells = row.findAll('td')               
                program['institution'] = cells[0].text
                program['title'] = cells[1].text 
                anchor = cells[1].find('a')
                program['url'] = anchor['href']
                program['type'] = program_type
                self.data.append(program)
            
