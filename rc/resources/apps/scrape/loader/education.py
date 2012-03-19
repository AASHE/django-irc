from django.db.models import get_model

from rc.resources.apps.scrape.loader import GenericLoader
from rc.resources.apps.education.models import CampusSustainabilityCourseTeacher


class AcademicCenterLoader(GenericLoader):

    def create_instance(self, data):
        from rc.resources.apps.education.models import AcademicCenterType
        
        center_types = dict( [(value, key) for key, value in
                              AcademicCenterType.CENTER_TYPES ])
        
        this_center_type, new_object = AcademicCenterType.objects.get_or_create(
            type=center_types.get(data['category'], ''))
        
        data['type'] = this_center_type
        super(AcademicCenterLoader, self).create_instance(data)

class CampusSustainabilityCourseLoader(GenericLoader):
    
    def create_instance(self, data):
        # each datum is a school, and each school can have >1 course.
        # since we're loading courses, not schools, we need to call
        # GenericLoader.create_instance() for each course.  note, this
        # breaks the pattern of create_instance() returning the db
        # object that was created.
        # if 'Aquinas' in data['school_name']:
        #     print "**** SKIPPING AQUINAS!! ****"
        #     return
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

