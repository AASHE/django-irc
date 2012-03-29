from django.db.models import get_model
from rc.resources.apps.policies.models import *
from rc.resources.apps.scrape.loader import BaseLoader, LoaderException


class PolicyLoader(BaseLoader):
    def __init__(self, parser_class, model_or_string, **kwargs):
        # prevent reset of Policy model since it is shared 
        super(PolicyLoader, self).__init__(parser_class, model_or_string, **kwargs)
        if self.kwargs.has_key('policy_type'):
            obj, created = PolicyType.objects.get_or_create(type=self.kwargs['policy_type'])
            self.policy_type = obj
        else:
            self.policy_type = None
        if self.kwargs.has_key('resource_area'):
            obj, created = ResourceArea.objects.get_or_create(
                area=self.kwargs['resource_area'])
            self.resource_area = obj
        else:
            self.resource_area = None
    
    def create_instance(self, data):
        obj = self.model()
        obj.title = data['title']
        obj.url = data['url']
        obj.description = data.get('notes', '')
        obj.notes = data['institution']
        obj.type = self.policy_type
        obj.resource_area = self.resource_area
        obj.save()
        return obj

    def load_all(self):
        self.parser.parsePage()
        for policy in self.parser.data:
            try:
                self.create_instance(policy)
            except:
                import sys, traceback                
                exc_type, exc_value, exc_tb = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_tb)
                raise LoaderException('%s failed to load parser %s for %s' % (
                        self.__class__.__name__, self.parser_class.__name__, self.model.__name__))
            
