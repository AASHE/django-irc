from rc.resources.apps.policies.models import PolicyType
from rc.resources.apps.scrape.loader.base import GenericLoader


class PolicyLoader(GenericLoader):

    def create_instance(self, data):
        '''
        Links a PolicyType, based on data['policy_type'], to the
        Policy that GenericLoader.create_instance() will make.
        '''
        type_obj, _ = PolicyType.objects.get_or_create(
            type=data.pop('policy_type'))
        data['type'] = type_obj
        return super(PolicyLoader, self).create_instance(data)
