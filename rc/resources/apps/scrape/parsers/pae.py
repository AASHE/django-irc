from base import PageParser, SimpleTableParser


BASE_URL = 'http://www.aashe.org/resources/'

class SustainabilityPlan(SimpleTableParser):
    '''
    >>> parser = SustainabilityPlan()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-sustainability-plans'
    login_required = True

class AlumniSustainabilityFunds(SimpleTableParser):
    '''
    >>> parser = AlumniSustainabilityFunds()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'alumni-sustainability-funds'
    login_required = True

class CampusMasterPlan(PageParser):
    '''
    >>> parser = CampusMasterPlan()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'master-plans-incorporate-sustainability'
    login_required = True

    def parsePage(self):
        paras = self.soup.find('div', {'class': 'content clear-block'}).findAll('p')
        data = {}
        for para in paras:
            strong = para.find('strong')
            anchor = para.find('a')
            br = para.find('br')
            if br:
                textEl = br.nextSibling
            else:
                textEl = ''
            data['institution'] = strong.text
            data['title'] = anchor.text
            data['url'] = dict(anchor.attrs).get('href', '')
            data['description'] = textEl
            if 'minor reference' in para.findPrevious('h2').text.lower():
                data['minor_reference_only'] = True
            self.data.append(data)
            data = {}

class AssessmentTools(PageParser):
    '''
    >>> parser = AssessmentTools()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-sustainability-assessment-tools'
    login_required = True

    def parsePage(self):
        paras = self.soup.find('div', {'class': 'content clear-block'}).findAll('p')
        data = {}
        for para in paras:
            anchor = para.find('a')
            br1 = para.find('br')
            br2 = br1.findNextSibling('br')
            em = para.find('em')
            textEl = br2.nextSibling
            data['institution'] = em.text
            data['url'] = dict(anchor.attrs).get('href', '')
            data['title'] = anchor.text
            data['description'] = textEl
            data['category'] = para.findPrevious('h2').text
            self.data.append(data)
            data = {}

class SustainabilityBlog(PageParser):
    '''
    >>> parser = SustainabilityBlog()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-sustainability-blogs'
    login_required = True

    def parsePage(self):
        table = self.soup.find('div', {'class': 'content clear-block'}).find('table')
        data = {}
        for li in table.findAll('li'):
            anchor = li.find('a')
            em = li.findPrevious('strong').find('em')
            data['title'] = anchor.text
            data['url'] = dict(anchor.attrs).get('href', '')
            data['type'] = em.text
            self.data.append(data)
            data = {}

class RevolvingFund(PageParser):
    '''
    >>> parser = RevolvingFund()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = BASE_URL + 'campus-sustainability-revolving-loan-funds'
    login_required = True

    def parsePage(self):
        uls = self.soup.find('div', {'class': 'content clear-block'}).findAll('ul')
        data = {}
        for ul in uls:
            para = ul.findPreviousSibling('p')
            strong = para.find('strong')
            br = para.find('br')
            textEl = br.nextSibling
            anchor = ul.find('li').find('a')
            data['institution'] = strong.text
            data['title'] = anchor.text
            data['url'] = dict(anchor.attrs).get('href','')
            data['description'] = textEl
            self.data.append(data)
            data = {}

class StudentFees(PageParser):
    '''
    >>> parser = StudentFees()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = (BASE_URL + 'mandatory-student-fees-renewable-energy-and-' +
           'energy-efficiency')
    login_required = False

    def parsePage(self):
        content_div = self.soup.find('div', {'class': 'content clear-block'})
        for org_name in content_div.findAll('strong'):
            description_element = org_name.parent.findNextSibling('p')
            fee_list = description_element.findNextSibling('ul')
            fees = list()
            for fee in fee_list.findAll('li'):
                anchor = fee.find('a')
                fees.append({'institution': org_name.text,
                             'url': anchor['href'],
                             'title': anchor.text})
            self.data.append({'institution': org_name.text,
                              'description': description_element.text,
                              'fees': fees})
