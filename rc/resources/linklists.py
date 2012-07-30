from linkcheck import Linklist
from resources.models import ResourceItem

class ResourceItemLinklist(Linklist):
    model = ResourceItem
    object_filter = {'active': True}
    url_fields = ['url',]
        
linklists = {'Resource Items': ResourceItemLinklist}