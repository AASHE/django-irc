from base import PageParser, SimpleTableParser


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

class AlumniSustainabilityFunds(SimpleTableParser):
    '''
    >>> parser = AlumniSustainabilityFunds()
    >>> parser.parsePage()
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/alumni-sustainability-funds'
    login_required = True

    def processTableData(self, row, els):
        policyData = {}
        policyData['institution'] = els[1].text
        anchor = els[3].find('a').extract()
        policyData['url'] = anchor['href']
        policyData['title'] = anchor.text
        policyData['notes'] = els[3].text
        return policyData

        policyData['url'] = anchor['href']

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

