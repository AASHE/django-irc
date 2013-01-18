from global_settings import *


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

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.flatpages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    'django.contrib.markup',
    'aashe.aashestrap',
    'aashe.organization',
    'aashe.aasheauth',
    'treemenus',
    'linkcheck',
    'rc.cms',
    'rc.resources',
    'rc.resources.apps.officers',
    'rc.resources.apps.policies',
    'rc.resources.apps.programs',
    'rc.resources.apps.education',
    'rc.resources.apps.operations',
    'rc.resources.apps.pae',
    'rc.resources.apps.scrape',
    'rc.resources.apps.revolving_fund',
    )
