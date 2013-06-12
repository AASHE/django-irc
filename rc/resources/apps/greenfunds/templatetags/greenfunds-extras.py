# https://docs.djangoproject.com/en/1.4/howto/custom-template-tags/#code-layout
from django import template

register = template.Library()

def model_name_filter(value):
    return value.__class__.__name__

register.filter('model_name_filter', model_name_filter)
