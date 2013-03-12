from django.contrib.localflavor.us import us_states
from django.contrib.localflavor.ca import ca_provinces
from django import template
from django.conf import settings
from django.template.defaultfilters import stringfilter



STATES_AND_PROVINCES = us_states.US_STATES + ca_provinces.PROVINCE_CHOICES

register = template.Library()

@register.filter
@stringfilter
def expand_state_abbrev(value):
    state_lookup = dict(STATES_AND_PROVINCES)
    if state_lookup.has_key(value):
        return state_lookup[value]
    else:
        return value
