import re
import string
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

    def processTable(self, table, headings=True, save_resources=True):
        '''If save_resource is True, the resources parsed get popped into
           self.data.  If not, the caller should append() or extend() them
           into self.data.
        '''
        # get all <tr> tags from the table...
        rows = row_tags = table.findAll('tr')
        # loop over each <tr> row and extract the content...
        if headings:
            rows = row_tags[1:]
        table_resources = []
        for row in rows:
            resource_items = self.processTableData(row)
            if resource_items:  # if row is empty, resource_items is, too
                table_resources.extend(resource_items)
        if save_resources:
            self.data.extend(table_resources)
        return table_resources

    def processTableData(self, row, institution_cell_num=0, anchor_cell_num=1):
        '''
        Overload this method in sub-classes to customize the table
        extraction process.

        row - the <tr> element
        institution_cell_num - index of cell that contains institution name
        anchor_cell_num - index of cell that contains resource url(s)
        '''
        cells = row.findAll('td')
        institution = cells[institution_cell_num].text
        # Multiple resource items for the same organization can be included
        # in the same table row.  Multiple anchors in a table cell indicate
        # this.  So we scrape these resources individually.
        resource_items = list()
        while True:
            try:
                anchor = cells[anchor_cell_num].find('a').extract()
            except AttributeError:
                break
            else:
                resource_item = {}
                resource_item['institution'] = institution
                resource_item['url'] = anchor['href']
                resource_item['title'] = anchor.text
                resource_items.append(resource_item)
        if cells[anchor_cell_num].text:
            resource_items[-1]['notes'] = self.text_to_notes(
                cells[anchor_cell_num].text)
        return resource_items

    def parsePage(self, headings=True):
        # data is in the first <table> on the page
        self.processTable(self.soup.findAll('table')[0], headings=headings)

    def text_to_notes(self, text):
        '''Filter text according to rules that define what should be
        saved as a note.

        This code is kind of bulky, but I hope the structure
        clearly indicates my intent.
        '''
        def cut_parentheticals(text):
            '''Cut parenthetical phrases out of text.'''
            return re.sub(r'\(.*?\)', '', text)

        def just_punctuation(text):
            '''Is text just a string of punctuation marks?'''
            return not bool(text.strip(string.punctuation))

        def just_and(text):
            '''Is text just "and" (maybe with punctuation)?'''
            return text.strip(string.punctuation).strip().lower() == 'and'

        notes_text = cut_parentheticals(text)
        if (not just_punctuation(notes_text) and
            not just_and(notes_text)):
            return notes_text
        else:
            return ''

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

    def processTableData(self, row):
        '''
        row - the <tr> element
        '''
        resources = super(ElectronicWasteParser, self).processTableData(row)
        if resources and len(row.findAll('td')) > 2:
            resources[-1]['items'] = row.findAll('td')[2].text
        return resources

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
