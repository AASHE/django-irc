from rc.resources.apps.programs import models
from rc.resources.apps.scrape.loader import GenericLoader


class ProgramLoader(GenericLoader):
    
    def create_instance(self, data):
        type_obj, created = models.ProgramType.objects.get_or_create(
            type=data['program_type'])
        data['type'] = type_obj
        del data['program_type']
        return super(ProgramLoader, self).create_instance(data)        

