from base import PageParser, SimpleTableParser
from BeautifulSoup import BeautifulSoup, NavigableString


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
    
class SustainabilityPlan(SimpleTableParser):
    '''
    >>> parser = SustainabilityPlan()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-sustainability-plans'
    login_required = True

class GlobalWarmingCommitments(SimpleTableParser):
    '''
    >>> parser = GlobalWarmingCommitments()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-global-warming-commitments'
    login_required = False

    def processTable(self, table, headings=True):
        # get all <tr> tags from the table...
        row_tags = table.findAll('tr')
        policyData = {}
        # loop over each <tr> row and extract the content...
        for row in row_tags[1:]:
            # get all the <td> tags in the <tr>...
            tags = [el for el in row]
            policyData['institution'] = tags[1].text
            policyData['url'] = dict(tags[3].first().attrs)['href']
            policyData['policy_name'] = tags[3].text
            policyData['commitment_date'] = tags[5].text
            self.data.append(policyData)
            policyData = {}

class CampusCaps(PageParser):
    '''
    >>> parser=CampusCaps()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-climate-action-plans'

    def parsePage(self):
        # ONLY the first table on this page is for CAPs, the other
        # is other campus climate action publications
        table = self.soup.findAll('table')[0]
        data = {}
        for row in table.findAll('tr')[1:]:
            tags = [el for el in row]
            data['institution'] = tags[1].text
            data['title'] = tags[3].text
            data['url'] = dict(tags[3].find('a').attrs).get('href','')
            data['formally_adopted'] = tags[3].find('strong') != None
            self.data.append(data)
            data = {}

class CampusOtherCAPPubs(PageParser):
    '''
    >>> parser=CampusOtherCAPPubs()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-climate-action-plans'

    def parsePage(self):
        table = self.soup.findAll('table')[1]
        data = {}
        for row in table.findAll('tr')[1:]:
            tags = [el for el in row]
            data['institution'] = tags[1].text
            data['title'] = tags[3].text
            data['url'] = dict(tags[3].find('a').attrs).get('href','')
            self.data.append(data)
            data = {}
            
class GlobalWarmingCommitment(PageParser):
    '''
    >>> parser=GlobalWarmingCommitment()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-global-warming-commitments'

    def parsePage(self):
        table = self.soup.findAll('table')[0]
        data = {}
        for row in table.findAll('tr')[1:]:
            tags = [el for el in row]
            data['institution'] = tags[1].text
            data['title'] = tags[3].text
            data['url'] = dict(tags[3].find('a').attrs).get('href','')
            data['date_of_commitment'] = tags[5].text
            self.data.append(data)
            data = {}        

class AlumniSustainabilityFunds(SimpleTableParser):
    '''
    >>> parser = AlumniSustainabilityFunds()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/alumni-sustainability-funds'
    login_required = True

class CampusMasterPlan(PageParser):
    '''
    >>> parser = CampusMasterPlan()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/master-plans-incorporate-sustainability'
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
            self.data.append(data)
            data = {}

class AssessmentTools(PageParser):
    '''
    >>> parser = AssessmentTools()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/campus-sustainability-assessment-tools'
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
    url = 'http://www.aashe.org/resources/campus-sustainability-blogs'
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
    url = 'http://www.aashe.org/resources/campus-sustainability-revolving-loan-funds'
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

