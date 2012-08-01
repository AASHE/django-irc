from linkcheck import Linklist
from rc.cms.models import Page

class PageLinklist(Linklist):
    model = Page
    object_filter = {'active': True}
    html_fields = ['content',]
        
linklists = {'Pages': PageLinklist}