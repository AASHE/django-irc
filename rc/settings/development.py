from global_settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aashe_rc_dev',
        'USER': 'aashe_rc',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
        }
    }

STATIC_ROOT = os.path.join(SITE_ROOT, '../../static')
STATIC_URL = 'http://www.aashedev.org/aashe-rc/static/'

# Haystack
HAYSTACK_SITECONF = 'rc.search_sites'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = os.path.join(SITE_ROOT, '../../whoosh_index')
