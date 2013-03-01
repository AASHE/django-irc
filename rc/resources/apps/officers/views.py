from django.views.generic.list import ListView
from rc.resources.apps.officers.models import *
from rc.resources.views import ResourceItemListView

class OfficerList(ResourceItemListView):
    allow_empty = True
    model = CampusSustainabilityOfficer
    queryset = CampusSustainabilityOfficer.objects.order_by('organization__picklist_name')