from django.db.models import get_model
from rc.resources.apps.policies.models import *


class LoaderException(Exception):
    pass

class BaseLoader(object):
    def __init__(self, parser_class, model_or_string, reset=False):
        '''
        Setup the loader with the parser_class to use and the model
        to dump the parser's data into. The model can be specified
        as an actual models.Model subclass or as a string that
        specifies the model in Django's `app.model` syntax.
        '''
        self.parser_class = parser_class
        self.parser = self.parser_class()
        self.reset = reset
        if isinstance(model_or_string, basestring):
            self.model = get_model(*model_or_string.split('.'))
        else:
            self.model = model_or_string
        if not self.model:
            raise ValueError("%s model_or_string kwarg must be valid Model subclass or Django app.Model string (%s)" % (self.__class__.__name__, self.parser_class.__name__))

    def reset_model(self):
        self.model.objects.all().delete()

    def create_instance(self, data):
        raise NotImplemented

class PolicyLoader(BaseLoader):
    def __init__(self, parser_class, model_or_string, policy_type):
        # prevent reset of Policy model since it is shared 
        super(PolicyLoader, self).__init__(parser_class, model_or_string)
        self.policy_type = PolicyType.objects.get(type=policy_type)
    
    def create_instance(self, data):
        obj = self.model()
        obj.title = data['title']
        obj.url = data['url']
        obj.description = data.get('notes', '')
        obj.notes = data['institution']
        obj.type = self.policy_type
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
            
class GenericLoader(BaseLoader):
    def create_instance(self, data):
        init_args = {}
        if data.has_key('institution'):
            try:
                inst_query = data['institution'].strip().lower()
                institution_obj = Organization.objects.get(name__iexact=inst_query)
                data['organization'] = institution_obj
            except:
                data['notes'] = "Institution is " + data['institution']
                del data['institution']
        # iterate over all the keys in the dictionary provided by
        # the parser... any keys that are fields on the model, use
        # to construct a new instance of the model
        for key in data.keys():
            if key in self.model._meta.get_all_field_names() and data[key]:
                init_args.update({key: data[key]})
        obj = self.model(**init_args)
        obj.save()
        return obj

    def load_all(self, reset=False):
        self.parser.parsePage()
        if self.reset:
            self.reset_model()
        for data in self.parser.data:
            try:
                self.create_instance(data)
            except:
                import sys, traceback                                
                exc_type, exc_value, exc_tb = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_tb)                
                raise LoaderException('%s failed to load parser %s for %s' % (
                        self.__class__.__name__, self.parser_class.__name__, self.model.__name__))

class BottleWaterBanLoader(GenericLoader):
    def create_instance(self, data):
        from rc.resources.apps.operations.models import BottledWaterBan
        ban_codes = dict([(value, key) for key, value in BottledWaterBan.BAN_TYPES])
        code = ban_codes.get(data['type'], '')
        data['type'] = code
        super(BottleWaterBanLoader, self).create_instance(data)

class CarShareLoader(GenericLoader):
    def create_instance(self, data):
        from rc.resources.apps.operations.models import CarSharePartner
        if data.has_key('partner'):
            try:
                partner_obj = CarSharePartner.objects.get(name=data['partner'])
            except CarSharePartner.DoesNotExist:
                partner_obj = CarSharePartner.objects.create(
                    name=data['partner'])
        data['partner'] = partner_obj
        data['title'] = data.get('institution', '')
        super(CarShareLoader, self).create_instance(data)

class GlobalWarmingLoader(GenericLoader):
    def create_instance(self, data):
        pass

class RecyclingWasteLoader(GenericLoader):
    def create_instance(self, data):
        from rc.resources.apps.operations.models import RecyclingWebsite
        super(RecyclingWasteLoader, self).create_instance(data)
        
class BuildingDashboardLoader(GenericLoader):
    def create_instance(self, data):
        from rc.resources.apps.operations.models import BuildingDashboard, BuildingDashboardPartner
        if data.has_key('manufacturer_type'):
            partner_obj, created = BuildingDashboardPartner.objects.get_or_create(name=data['manufacturer_type'])
            data['partner'] = partner_obj
            del data['manufacturer_type']
        super(BuildingDashboardLoader, self).create_instance(data)

class BiodieselFleetLoader(GenericLoader):
    def create_instance(self, data):
        from rc.resources.apps.operations.models import BiodieselFleet
        production_types = dict([(value, key) for key, value in BiodieselFleet.PRODUCTION_TYPE])
        production_type = production_types.get(data['biodiesel_source'], '')
        data['biodiesel_source'] = production_type
        super(BiodieselFleetLoader, self).create_instance(data)
        
class CarBanLoader(GenericLoader):
    def create_instance(self, data):
        from rc.resources.apps.operations.models import CarBan
        ban_types = dict([(value, key) for key, value in CarBan.BAN_TYPES])
        ban_type = ban_types.get(data['type'], '')
        data['type'] = ban_type
        super(CarBanLoader, self).create_instance(data)
        
class SustainableDiningInitiativesLoader(GenericLoader):
    def create_instance(self, data):
        from rc.resources.apps.operations.models import DiningInitiative
        ownership_types = dict([(value, key) for key, value in DiningInitiative.OWNERS])
        ownership_type = ownership_types.get(data['type'], '')
        data['ownership'] = ownership_type
        super(SustainableDiningInitiativesLoader, self).create_instance(data)

class WindTurbineLoader(GenericLoader):
    def create_instance(self, data):
        data['capacity'] = data['capacity'].strip(',')
        super(WindTurbineLoader, self).create_instance(data)
        
class TransitPassLoader(GenericLoader):
    def create_instance(self, data):
        from rc.resources.apps.operations.models import TransitPass
        pass_types = dict([(value, key) for key, value in TransitPass.PASS_TYPES])
        pass_type = pass_types.get(data['type'], '')
        data['type'] = pass_type
        super(TransitPassLoader, self).create_instance(data)

class SustainabilityPurchasingLoader(GenericLoader):
    def create_instance(self, data):
        from rc.resources.apps.operations.models import PurchasingLink
        link_types = dict([(value, key) for key, value in PurchasingLink.LINK_TYPES])
        link_type = link_types.get(data['type'], '')
        data['type'] = link_type
        super(SustainabilityPurchasingLoader, self).create_instance(data)
        
class GreenBuildingLoader(GenericLoader):
    def create_instance(self, data):
        from rc.resources.apps.operations.models import GreenBuildingType
        if data.has_key('type'):
            try:
                type_obj = GreenBuildingType.objects.get(name=data['type'])
            except CarSharePartner.DoesNotExist:
                type_obj = GreenBuildingType.objects.create(
                    name=data['type'])
        data['type'] = type_obj
        super(GreenBuildingLoader, self).create_instance(data)
            
