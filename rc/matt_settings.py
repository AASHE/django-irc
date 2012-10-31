from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_irc_dev',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
        }
    }

STATIC_ROOT = os.path.join(SITE_ROOT, '../static')

# Production Drupal Services settings
AASHE_DRUPAL_URI = "http://www.aashe.org/services/xmlrpc"
AASHE_DRUPAL_KEY = "15cf217790e3d45199aeb862f73ab2ff"
AASHE_DRUPAL_KEY_DOMAIN = "acupcc.aashe.org"
AASHE_DRUPAL_COOKIE_SESSION = "SESS0e65dd9c18edb0e7e84759989a5ca2d3"
AASHE_DRUPAL_COOKIE_DOMAIN = ".aashe.org"
