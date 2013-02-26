from global_settings import *

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

SALESFORCE_USERNAME=os.environ.get("SALESFORCE_USERNAME", None)
SALESFORCE_PASSWORD=os.environ.get("SALESFORCE_PASSWORD", None)

# Haystack
HAYSTACK_SITECONF = 'rc.search_sites'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = os.path.join(SITE_ROOT, '../../whoosh_index')

# Moderation System
MODERATORS = ('resources@aashe.org', 'niles@aashe.org', 'jesse.legg@aashe.org')
