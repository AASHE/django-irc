# https://docs.djangoproject.com/en/1.4/howto/custom-template-tags/#code-layout
from django import template
from django.db.models import get_model

register = template.Library()

def model_name_filter(value):
    return value.__class__.__name__

register.filter('model_name_filter', model_name_filter)

def model_verbose_name_filter(value):
    model = get_model(*value.split('.'))
    return model._meta.verbose_name

register.filter('model_verbose_name_filter', model_verbose_name_filter)
