from global_settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_irc_dev',
        'USER': 'django_irc_dev',
        'PASSWORD': 'te86FRas',
        'HOST': 'rc2-dev.aashe.org',
        'PORT': '',
        }
    }

STATIC_ROOT = os.path.join(SITE_ROOT, '../static')
