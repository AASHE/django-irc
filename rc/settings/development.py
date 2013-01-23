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
