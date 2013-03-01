from linkcheck import Linklist
from rc.resources.apps.education.models import CampusSustainabilityCourseTeacher

class CampusSustainabilityCourseTeacherLinklist(Linklist):
    model = CampusSustainabilityCourseTeacher
    object_filter = {}
    url_fields = ['web_page',]
        
linklists = {'SustainabilityCourseTeachers': CampusSustainabilityCourseTeacherLinklist}