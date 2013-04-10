from global_settings import *
try:
    from salesforce import *
except:
    pass

DEBUG = True

INTERNAL_IPS = ('127.0.0.1',)

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

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.flatpages',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',
    'django.contrib.humanize',
    'aashe.aashestrap',
    'aashe.organization',
    'aashe.aasheauth',
    'aashe.moderation',
    'aashe.disciplines',
    'aashe.departments',
    'treemenus',
    'linkcheck',
    'haystack',
    'geopy',
    'rc.cms',
    'rc.resources',
    'rc.resources.apps.officers',
    'rc.resources.apps.policies',
    'rc.resources.apps.programs',
    'rc.resources.apps.education',
    'rc.resources.apps.operations',
    'rc.resources.apps.pae',
    'rc.resources.apps.scrape',
    'rc.resources.apps.academic_programs',
    'rc.resources.apps.revolving_fund',
    'rc.resources.apps.greenfunds',
    'pagedown',
    'debug_toolbar'
    )

# Search config
LINKCHECK_GOOGLE_API_KEY = "AIzaSyDmTsmmVnqeGUfjeeMa4WeFO4rZDJzQ2us"
LINKCHECK_GOOGLE_CX = "014955680860349223306:vapi7echb7m"
