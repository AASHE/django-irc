import re
import string

from aashe.organization.models import Organization
from BeautifulSoup import BeautifulSoup
from django.conf import settings
from rc.resources.apps.scrape.parsers.base import PageParser
from rc.resources.apps.officers.models import CampusSustainabilityOfficer

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
        data = {}
        self.soup.prettify()
        content = self.soup.find('div', {'class': 'content clear-block'})
        paras = content.findAll('p')
        for element in paras[3:]:
            # org name is always first strong tag
            data['organization_name'] = element.find('strong').text
            try:
              # full name is always first a after org name
              anchor = element.find('a')
              data['full_name'] = anchor.text
              data['title'] = dict(anchor.attrs).get('href','').replace('mailto:', '')
              # title is always after name
              title = anchor.nextSibling.nextSibling
              data['title'] = title.replace('\n', '')
            # exception for texas a&m, whose email address isn't on the directory
            except:
              pass
              
            try:
              # this is where things get tricky, next could be department or phone number
              first_suspect = title.nextSibling.nextSibling
              if first_suspect.replace('\n', '').startswith("("):
                data['phone'] = first_suspect.replace('\n', '')
              else:
                data['department'] = first_suspect.replace('\n', '')
                try: 
                  if first_suspect.nextSibling.nextSibling.replace('\n', '').startswith("("):
                    data['phone'] = first_suspect.nextSibling.nextSibling.replace('\n', '')
                except:
                  pass
              # ignore multiple urls
              data['web_page'] = anchor.findNextSibling('a')
            except:
              pass
            
            # do not remove
            self.data.append(data)
            data = {}
    
              

# Loader for data parsed by OfficerParser
class OfficerLoader(object):
  '''
  from rc.resources.apps.officers.parser import OfficerLoader
  loader = OfficerLoader()
  loader.save()
  '''
  
  def save(self):
      parser = OfficerParser()
      parser.parsePage()
      for element in parser.data:
        # create or update officer objects
          obj, created = CampusSustainabilityOfficer.objects.get_or_create(full_name=element['full_name'],
                          defaults={'title': element['title'],
                                    'email': element['email'],
                                    'phone': element['phone'],
                                    'organization': organization,
                                    'web_page': element['web_page']})
          obj.save()
          