from django.views.generic.list import ListView
from rc.resources.apps.officers.models import models

class OfficerList(ListView):
    allow_empty = True
    model = CampusSustainabilityOfficer