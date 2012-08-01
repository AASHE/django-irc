from linkcheck import Linklist
from rc.resources.apps.programs.models import Program, ElectronicWasteProgram
        
# class ProgramLinklist(Linklist):
#     model = Program
#     object_filter = {}
#     url_fields = ['url',]
#         
# linklists = {'Programs': ProgramLinklist}

class ElectronicWasteProgramLinkList(Linklist):
    model = ElectronicWasteProgram
    object_filter = {}
    url_fields = ['url',]
        
linklists = {'Electronic Waste Programs': ElectronicWasteProgramLinkList}