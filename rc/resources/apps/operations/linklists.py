from linkcheck import Linklist
from rc.resources.apps.operations.models import CampusGreenBuildingLink

class CampusGreenBuildingLinkLinklist(Linklist):
    model = CampusGreenBuildingLink
    object_filter = {}
    url_fields = ['url',]
        
linklists = {CampusGreenBuildingLink._meta.verbose_name: CampusGreenBuildingLinkLinklist}