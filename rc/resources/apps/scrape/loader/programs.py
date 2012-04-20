from rc.resources.apps.programs.models import ProgramType
from rc.resources.apps.scrape.loader import GenericLoader


class ProgramLoader(GenericLoader):

    def create_instance(self, data):
        '''
        Links a ProgramType, based on data['program_type'], to the
        Program that GenericLoader.create_instance() will make.
        '''
        type_obj, _ = ProgramType.objects.get_or_create(
            type=data.pop('program_type'))
        data['type'] = type_obj
        return super(ProgramLoader, self).create_instance(data)
