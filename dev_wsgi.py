#! /usr/bin/env python
import sys
import os
import django.core.handlers.wsgi
sys.path.append('/var/www/django_projects/aashe-rc/aashe-rc')
os.environ['DJANGO_SETTINGS_MODULE'] = 'rc.settings'
application = django.core.handlers.wsgi.WSGIHandler()
