from linkcheck import Linklist
from rc.resources.models import ResourceItem
        
class ResourceItemLinklist(Linklist):
    model = ResourceItem
    object_filter = {}
    url_fields = ['url',]
        
linklists = {'Resource Items': ResourceItemLinklist}