import urllib, urllib2
from BeautifulSoup import BeautifulSoup


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
            if policyData:  # if row is empty, policyData is None
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
        anchor = els[3].find('a').extract()
        policyData['url'] = anchor['href']
        policyData['title'] = anchor.text
        if els[3].text:
            policyData['notes'] = els[3].text
        return policyData

    def parsePage(self, headings=True):
        # data is in the first <table> on the page
        self.processTable(self.soup.findAll('table')[0], headings=headings)


class ElectronicWasteParser(SimpleTableParser):
    '''
    The electronic waste page has three kinds of resources on it; policies,
    programs, and events.  This parser is pushed into the base module so
    the parsers for each of those apps can use it.

    >>> parser=ElectronicWaste()
    >>> parser.parsePage('events')
    >>> len(parser.data) != 0
    True
    '''
    url = 'http://www.aashe.org/resources/e-waste-programs-policies-and-events'
    login_required = True

    def processTableData(self, row, els):
        '''
        row - the <tr> element
        els - the elements of row
        '''
        # sometimes an empty row is inserted into a table.  it doesn't
        # show to the viewer, on the page, but it screws this up.
        if not row.text:
            return
        cells = row.findAll('td')
        data = {}
        data['institution'] = cells[0].text
        anchor = cells[1].find('a').extract()
        data['url'] = anchor['href']
        data['title'] = anchor.text
        # notes are in the third column, or tucked into the second column,
        # after the anchor:
        try:
            data['notes'] = cells[2].text
        except IndexError:
            data['notes'] = cells[1].text
        return data

    def parsePage(self, resource_name=None):
        def header_texts(table):
            headers = table.findAll('th')
            return [ h.text.lower() for h in headers ]
        resource_names = ('events', 'policies', 'programs')
        if resource_name.lower() not in resource_names:
            raise Exception('valid resource names are {0} (not {1})'.format(
                resource_names, resource_name))
        tables = self.soup.findAll('table')
        resource_table = [ t for t in tables
                           if resource_name.lower() in header_texts(t) ][0]
        self.processTable(resource_table, headings=True)
