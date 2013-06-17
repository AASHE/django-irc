import os
from global_settings import *

DEBUG=True

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
    'NAME': 'aashe_rc_dev', # Or path to database file if using sqlite3.
    'USER': 'aashe_rc', # Not used with sqlite3.
    'PASSWORD': '', # Not used with sqlite3.
    'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
    'PORT': '', # Set to empty string for default. Not used with sqlite3.
    'OPTIONS': {
       'init_command': 'SET storage_engine=MYISAM',
    }
    }
 }
SITE_ROOT = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
STATIC_ROOT = os.path.join(SITE_ROOT, '../../static')
STATIC_URL = '/static/'

# Haystack
HAYSTACK_SITECONF = 'rc.search_sites'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = os.path.join(SITE_ROOT, '../../whoosh_index')

SALESFORCE_USERNAME=os.environ.get("SALESFORCE_USERNAME", None)
SALESFORCE_PASSWORD=os.environ.get("SALESFORCE_PASSWORD", None)

# Use a fake test analytics key when used with the aashe
# google_analytics context processor this will output the analytics
# Javascript, but not actually record hits
GOOGLE_ANALYTICS_KEY = 'xxxxxxxx'
