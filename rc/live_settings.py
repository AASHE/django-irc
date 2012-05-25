from settings import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_irc_production',
        'USER': 'django_irc',
        'PASSWORD': 'RHEzfK3Jn75JDVUt',
        'HOST': '10.176.128.183',
        'PORT': '',
        }
    }

STATIC_ROOT = os.path.join(SITE_ROOT, '../static')