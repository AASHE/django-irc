from django.db.models import get_model
from rc.resources.apps.policies.models import *

class AssessmentToolsLoader(GenericLoader):
    def create_instance(self, data):
        from rc.resources.apps.pae.models import AssessmentTool
        provider_types = dict([(value, key) for key, value in AssessmentTool.CREATORS])
        provider = provider_types.get(data['type'], '')
        data['provider'] = provider
        super(AssessmentToolsLoader, self).create_instance(data)