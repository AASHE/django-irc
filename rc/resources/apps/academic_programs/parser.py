import re
import htmlentitydefs
import string
import urllib, urllib2

from aashe.disciplines.models import Discipline
from BeautifulSoup import BeautifulSoup
from django.conf import settings
from rc.resources.apps.academic_programs.models import *


class ProgramParser(object):
    '''
    from apps.scrape.parser import ProgramParser
    parser = ProgramParser()
    parser.process()
    parser.data
    '''
    data = []
    
    def process(self):
        html = urllib.urlopen("http://www.aashe.org/resources/academic-programs/export").read()
        soup = BeautifulSoup(html)
        data = {}
        for element in soup.findAll('node'):
            # Populate row data
            data['title'] = unescape(getattr(element.find('title'), 'string', None).string)
            data['institution'] = getattr(element.find('institution'), 'string', None)
            data['other-institution'] = getattr(element.find('other-organization'), 'string', None)
            data['account'] = getattr(element.find('account'), 'string', None)
            # try to deal with the html in the description field
            # if this excepts, it's probably an empty field
            try:
              data['description'] = unescape(getattr(element.find('program-description'), 'string', None).string)
            except:
              data['description'] = None
            data['program_type'] = getattr(element.find('program-type'), 'string', None)
            data['homepage'] = getattr(element.find('program-homepage'), 'string', None)
            data['department'] = getattr(element.find('program-department'), 'string', None)
            data['duration'] = getattr(element.find('program-duration'), 'string', None)
            data['founded'] = getattr(element.find('year-founded'), 'string', None)
            data['distance_ed'] = getattr(element.find('distance-or-local'), 'string', None)
            data['commitment'] = getattr(element.find('program-commitment'), 'string', None)
            data['language'] = getattr(element.find('language-of-instruction'), 'string', None)
            data['blog'] = getattr(element.find('program-blog'), 'string', None)
            data['linkedin'] = getattr(element.find('program-linkedin-page'), 'string', None)
            data['facebook'] = getattr(element.find('program-facebook-page'), 'string', None)
            data['twitter'] = getattr(element.find('program-twitter-page'), 'string', None)
            data['discipline'] = getattr(element.find('program-discipline'), 'string', None)
            data['created_date'] = getattr(element.find('post-date'), 'string', None)
            data['updated_date'] = getattr(element.find('updated-date'), 'string', None)
            data['city'] = getattr(element.find('city'), 'string', None)
            data['state'] = getattr(element.find('state'), 'string', None)
            data['location-name'] = getattr(element.find('location-name'), 'string', None)
            # Write the above into data
            self.data.append(data)
            data = {}

# Loader for data parsed by ProgramParser
class ProgramLoader(object):
  '''
  from apps.scrape.parser import *
  loader = ProgramLoader()
  loader.save()
  '''
  
  def save(self):
      parser = ProgramParser()
      parser.process()
      
      for element in parser.data:
          
          # handle program types, disciplines, and filter institutions
          # all of these are foreign key fields
          try:
            discipline = Discipline.objects.get(name=unicode(element['discipline']))
          except:
            discipline = None
            
          try:
            organization = Organization.objects.get(account_num=unicode(element['account']))
          except:
            # TODO attempt to reconcile organization
            # if institution is set, use regex
            # institution name is set as unicode(element['institution'])
            # also we can try using unicode(element['other-institution'])
            # maybe something like Organization.objects.get(picklist_name__regex="whatever")
            try:
              organization = Organization.objects.get(picklist_name__regex=unicode(element['other-institution']))
            except:
              organization = None
            
          try:
            program_type = ProgramType.objects.get(name=unicode(element['program_type']))
          except:
            program_type = None

          # create or update material objects
          type_string = unicode(element['program_type'].string)
          ptype = ProgramType.objects.get(name=type_string)
          
          # Handle Distance Ed
          distance_types = dict([(value, key) for key, value in
                                 DISTANCE_CHOICES])
          distance_ed = distance_types.get(element['distance_ed'], '')
          
          # Handle Commitment
          commitment_types = dict([(value, key) for key, value in
                                 COMMITMENT_CHOICES])
          commitment = commitment_types.get(element['commitment'], '')
          
          obj, created = AcademicProgram.objects.get_or_create(homepage=unicode(element['homepage']),
                defaults={
                'title': element['title'],
                'location_name': (element['location-name'] or ''),
                'institution': organization,
                'other_inst': (element['other-institution'] or ''),
                'city': (element['city'] or ''),
                'state': (element['state'] or ''),
                'description': (element['description'] or ''),
                'program_type': ptype,
                'homepage': (element['homepage'] or ''),
                'department': (element['department'] or ''),
                'duration': (element['duration'] or ''),
                'founded': (element['founded'] or ''),
                'distance_ed': distance_ed,
                'commitment': commitment,
                'language': (element['language'] or ''),
                'blog': (element['blog'] or ''),
                'linkedin': (element['linkedin'] or ''),
                'facebook': (element['facebook'] or ''),
                'twitter': (element['twitter'] or ''),
                'discipline': discipline,
                'published': True,
                'created_date': element['created_date'],
                'updated_date': element['updated_date'],
                })
          
          # if organization:
          #   obj.institution.add(organization)
          # else:
          #   pass
            
def unescape(text):
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)