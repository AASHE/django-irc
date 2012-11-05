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
              data['email'] = dict(anchor.attrs).get('href','').replace('mailto:', '')
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
              page = anchor.findNextSibling('a')
              data['web_page'] = dict(page.attrs).get('href','')
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
      # delete all existing objects
      CampusSustainabilityOfficer.objects.all().delete()
      
      for element in parser.data:
        # these keys may not exist, so...
        try:
          title = element['title']
        except:
          title = ""
        try:
          email = element['email']
        except:
          email = ""
        try:
          phone = element['phone']
        except:
          phone = ""
        try:
          department = element['department']
        except:
          department = ""
        try:
          organization = Organization.objects.get(name=element['organization_name'])
        except:
          organization = None
        try:
          web_page = element['web_page']
          if web_page == None:
            web_page = ""
        except:
          web_page = ""
        # create or update officer objects
        obj, created = CampusSustainabilityOfficer.objects.get_or_create(full_name=element['full_name'],
                          defaults={'title': title,
                                    'email': email,
                                    'phone': phone,
                                    'organization': organization,
                                    'department': department,
                                    'web_page': web_page,})
        # if not created:
        #   # TODO update here
        #   obj.save()
          