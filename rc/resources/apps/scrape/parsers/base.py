import urllib, urllib2
from BeautifulSoup import BeautifulSoup, NavigableString


from django.conf import settings
username = settings.AASHE_ACCOUNT_USERNAME
password = settings.AASHE_ACCOUNT_PASSWORD

AASHEOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
urllib2.install_opener(AASHEOpener)

class PageParser(object):
    url = None
    login_required = False

    def _login(self):
        # TODO: Add 'if not AASHEOpener.is_logged_in'
        post_url = 'http://www.aashe.org/user/login'
        params = urllib.urlencode({'name': username,
                                   'pass': password,
                                   'form_id': 'user_login',
                                   'form_build_id': 'form-b0528de66df7ca2ec1ff2a7a86868049'})
        f = AASHEOpener.open(post_url, params)
        data = f.read()
        f.close()
    
    def __init__(self):
        if self.url:
            if self.login_required:
                self._login()
            self.page = AASHEOpener.open(self.url)
            self.soup = BeautifulSoup(
                self.page, convertEntities=BeautifulSoup.HTML_ENTITIES)
            
            self.data = []

    def parsePage(self):
        raise NotImplemented


class SimpleTableParser(PageParser):
    def processTable(self, table, headings=True):
        # get all <tr> tags from the table...
        rows = row_tags = table.findAll('tr')
        policyData = {}
        # loop over each <tr> row and extract the content...
        if headings:
            rows = row_tags[1:]
        for row in rows:
            # get all the <td> tags in the <tr>...
            tags = [el for el in row]
            policyData = self.processTableData(row, tags)
            self.data.append(policyData)
            policyData = {}

    def processTableData(self, row, els):
        '''
        Overload this method in sub-classes to customize the table
        extraction process.
        
        row - the <tr> element
        els - the elements inside the <tr> element, not technically
               "tags", because this is including text node elements, etc.
        '''        
        policyData = {}
        policyData['institution'] = els[1].text
        policyData['url'] = dict(els[3].first().attrs)['href']
        policyData['title'] = els[3].text
        return policyData
    
    def parsePage(self, headings=True):
        # data is in the first <table> on the page
        self.processTable(self.soup.findAll('table')[0], headings=headings)
    
