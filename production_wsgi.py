#! /usr/bin/env python
import sys
import os
import django.core.handlers.wsgi
sys.path.append('/var/www/django_projects/aashe-rc/current')
os.environ['DJANGO_SETTINGS_MODULE'] = 'rc.live_settings'
application = django.core.handlers.wsgi.WSGIHandler()
