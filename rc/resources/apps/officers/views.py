from django.views.generic.list import ListView
from rc.resources.apps.officers.models import *

class OfficerList(ListView):
    allow_empty = True
    model = CampusSustainabilityOfficer