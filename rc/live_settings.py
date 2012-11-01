from settings import *

DEBUG = False

# Email address the project will use to send notifications from
DEFAULT_FROM_EMAIL = 'www-data@aashe.org'

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

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'http://media.aashe.org/resources/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = 'http://media.aashe.org/resources/admin/'

# Settings for aashe.organization.sync and ISS replication
AASHE_ISS_DATABASE = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'iss',
    'USER': 'django_irc',
    'PASSWORD': 'RHEzfK3Jn75JDVUt',
    'HOST': '10.176.128.183',
    'PORT': '',
    }
AASHE_ISS_ORG_TABLE = 'organizations'
AASHE_ISS_DELETION_TABLE = 'acct_deletions'

# AASHE_DRUPAL_REQUIRED_ROLES = ('Staff', 'Content Administrator')
