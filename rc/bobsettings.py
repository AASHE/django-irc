# Bob's dev Django settings for rc project.
from settings import *

INSTALLED_APPS = INSTALLED_APPS + ('django_extensions',
				   'template_repl')

INTERNAL_IPS = ('127.0.0.1',)
