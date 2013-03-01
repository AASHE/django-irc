from global_settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_irc_production',
        'USER': 'django_irc',
        'PASSWORD': 'RHEzfK3Jn75JDVUt',
        'HOST': 'aashe-db.csl4c2c6dzyx.us-east-1.rds.amazonaws.com',
        'PORT': '',
        }
    }

STATIC_ROOT = os.path.join(SITE_ROOT, '../static')

# Settings for aashe.organization.sync and ISS replication
AASHE_ISS_DATABASE = {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'iss',
    'USER': 'django_irc',
    'PASSWORD': 'RHEzfK3Jn75JDVUt',
    'HOST': 'aashe-db.csl4c2c6dzyx.us-east-1.rds.amazonaws.com',
    'PORT': '',
    }
AASHE_ISS_ORG_TABLE = 'organizations'
AASHE_ISS_DELETION_TABLE = 'acct_deletions'
