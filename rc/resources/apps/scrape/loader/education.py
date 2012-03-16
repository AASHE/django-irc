from django.db.models import get_model

from rc.resources.apps.scrape.loader import GenericLoader


class AcademicCenterLoader(GenericLoader):

    def create_instance(self, data):
        from rc.resources.apps.education.models import AcademicCenterType
        
        center_types = dict( [(value, key) for key, value in AcademicCenterType.CENTER_TYPES ])
        
        this_center_type, new_object = AcademicCenterType.objects.get_or_create(
            type=center_types.get(data['category'], ''))
        
        data['type'] = this_center_type
        super(AcademicCenterLoader, self).create_instance(data)

