import re
import string
import urllib, urllib2

from aashe.organization.models import Organization
from BeautifulSoup import BeautifulSoup
from django.conf import settings

from rc.resources.apps.scrape.parsers import *


class OfficerParser(PageParser):
    '''
    from rc.resources.apps.officers.parser import OfficerParser
    parser = OfficerParser()
    parser.parsePage()
    parser.data
    '''
    url = "http://www.aashe.org/resources/directory-campus-sustainability-officers"
    login_required = True
    
    def parsePage(self):
        html = urllib.urlopen(self.url).read()
        soup = BeautifulSoup(html)
        data = {}
        content = soup.find('div', {'class': 'content clear-block'})
        import pdb
        pdb.set_trace()
        for element in content.findAll('p'):
            data = element
            self.data.append(data)
            print element.text
            data = {}
            # do stuff
            # anchor = element.find('a')
            #             br = element.find('br')
            #             foundin = element.find('span', {'class': 'searchreturndetails'})
            #             text = foundin.nextSibling.nextSibling
            #             data['title'] = anchor.text
            #             data['link'] = dict(anchor.attrs).get('href','')
            #             data['desc'] = text
            #             data['category'] = foundin.text
            #             print data['title']
            #             self.data.append(data)
            #             data = {}
    
              

# Loader for data parsed by SercParser
class OfficerLoader(object):
  '''
  from commons.apps.scrape.parsers.serc import *
  loader = SercLoader()
  loader.save()
  '''
  
  def save(self):
      parser = OfficerParser()
      parser.process()
      #for element in parser.data:
          # create or update material objects
          