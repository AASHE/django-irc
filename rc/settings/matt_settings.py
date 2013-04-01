from global_settings import *
# from salesforce import *

DEBUG = True

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

# Search config
LINKCHECK_GOOGLE_API_KEY = "AIzaSyDmTsmmVnqeGUfjeeMa4WeFO4rZDJzQ2us"
LINKCHECK_GOOGLE_CX = "014955680860349223306:vapi7echb7m"
