from linkcheck import Linklist
from resources.models import ResourceItem

class ResourceItemLinklist(Linklist):
    model = ResourceItem
    object_filter = {'active': True}
    html_fields = ['description', 'url',]
        
linklists = {'Pages': PageLinklist}