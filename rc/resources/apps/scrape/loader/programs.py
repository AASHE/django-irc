from rc.resources.apps.programs import models
from rc.resources.apps.scrape.loader import GenericResourceAreaLoader


class ProgramLoader(GenericResourceAreaLoader):

    def create_instance(self, data):
        '''
        Links a ProgramType, based on data['program_type'], to the
        Program that GenericLoader.create_instance() will make.
        '''
        type_obj, created = models.ProgramType.objects.get_or_create(
            type=data['program_type'])
        data['type'] = type_obj
        del data['program_type']
        return super(ProgramLoader, self).create_instance(data)
