from django.views.generic.list import ListView
from rc.academic_programs.models import AcademicProgram

class StudyList(ListView):
    allow_empty = True
    model = AcademicProgram
    paginate_by = 50