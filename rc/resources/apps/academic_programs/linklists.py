from linkcheck import Linklist
from rc.resources.apps.academic_programs.models import AcademicProgram

class AcademicProgramLinklist(Linklist):
    model = AcademicProgram
    object_filter = {}
    url_fields = ['homepage',]
    search_fields = ['title', 'institution',]
        
linklists = {AcademicProgram._meta.verbose_name: AcademicProgramLinklist}