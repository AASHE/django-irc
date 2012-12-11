from rc.resources.apps.scrape.loader import GenericLoader
from rc.resources.apps.education.models import AcademicCenter, \
     AcademicCenterType
from rc.resources.apps.education.models import CampusSustainabilityCourseTeacher
from rc.resources.apps.education.models import StudyAbroadProgram
from aashe.organization.models import Organization


ACADEMIC_CENTERS_RESET_YET = False


class AcademicCenterLoader(GenericLoader):

    def __init__(self, parser_class, model_or_string, reset=False):
        '''AcademicCenters are loaded by a bunch of parsers.  If we
        reset after each one, only the last one in remains.  So here
        we intercept the reset flag, and do it only once.
        '''
        global ACADEMIC_CENTERS_RESET_YET
        if reset and not ACADEMIC_CENTERS_RESET_YET:
            AcademicCenter.objects.all().delete()
            # since AcademicCenterTypes are created as side effect in
            # get_center_type() below, better blow 'em away here, too:
            AcademicCenterType.objects.all().delete()
            ACADEMIC_CENTERS_RESET_YET = True
        super(AcademicCenterLoader, self).__init__(parser_class,
                                                   model_or_string,
                                                   reset=False)
    
    def create_instance(self, data):
        data['type'] = self.get_center_type(data['category'])
        super(AcademicCenterLoader, self).create_instance(data)

    def get_center_type(self, type_code):
        '''
        Return the AcademicCenterType for type_code, creating it
        if necessary.
        '''
        center_types = dict(AcademicCenterType.CENTER_TYPES)
        center_type, new_object = AcademicCenterType.objects.get_or_create(
            **{'type': type_code})
        if new_object:
            center_type.description = center_types[type_code]
            center_type.save()
        return center_type


class CampusSustainabilityCourseLoader(GenericLoader):

    def create_instance(self, data):
        # each datum is a school, and each school can have >1 course.
        # since we're loading courses, not schools, we need to call
        # GenericLoader.create_instance() for each course.  note, this
        # breaks the pattern of create_instance() returning the db
        # object that was created.
        for course in data['courses']:
            course['institution'] = data['school_name']
            # save off the course teachers since GenericLoader.create_instance()
            # doesn't like keyword arguments that are lists:
            teachers = course['teachers']
            del(course['teachers'])
            course_on_sustainability = super(CampusSustainabilityCourseLoader, 
                                             self).create_instance(course)

            # attach instanc(es) of CoursesOnSustainabilityTeacher:
            for teacher in self.teacher_instances(teacher_data=teachers):
                course_on_sustainability.teachers.add(teacher)
                course_on_sustainability.save()

    def teacher_instances(self, teacher_data):
        csc_teachers = list()
        for teacher in teacher_data:
            csc_teacher, created = \
                CampusSustainabilityCourseTeacher.objects.get_or_create(
                    **teacher)
            csc_teacher.save()
            csc_teachers.append(csc_teacher)
        return csc_teachers

    def reset_model(self):
        CampusSustainabilityCourseTeacher.objects.all().delete()
        super(CampusSustainabilityCourseLoader, self).reset_model()

class StudyAbroadProgramLoader(GenericLoader):
    def create_instance(self, data):
        # if no matching institution exists, create one
        if data.has_key('institution'):
            try:
                inst_query = data['institution'].strip().lower()
                institution_obj = Organization.objects.get(
                    name__iexact=inst_query)
                data['organization'] = institution_obj
            except:
                Organization.objects.create(
                    name=data['institution'], picklist_name=data['institution'])
        super(StudyAbroadProgramLoader, self).create_instance(data)

