from django.db.models import get_model
from rc.resources.apps.policies.models import *
from rc.resources.apps.scrape.loader import GenericLoader, LoaderException


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
        if data['capacity'].lower() == 'unknown':
            del(data['capacity']) # Will load into db as a null.
        else:
            data['capacity'] = data['capacity'].replace(',', '')
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

class HybridFleetLoader(GenericLoader):
    def create_instance(self, data):
        # sometimes number of vehicles is '>1'; can't convert that
        # into an integer field, so we change it to 1:
        data['number'] = str(data['number']).translate(None, '>&gt;')
        
class GreenBuildingLoader(GenericLoader):
    def create_instance(self, data):
        from rc.resources.apps.operations.models import GreenBuildingType
        if data.has_key('type'):
            try:
                type_obj = GreenBuildingType.objects.get(type=data['type'])
            except GreenBuildingType.DoesNotExist:
                type_obj = GreenBuildingType.objects.create(
                    type=data['type'])
            data['type'] = type_obj
        super(GreenBuildingLoader, self).create_instance(data)

class CommuterSurveyLoader(GenericLoader):
    def create_instance(self, data):
        from rc.resources.apps.operations.models import CommuterSurvey
        survey_types = dict([(value, key) for key, value in CommuterSurvey.SURVEY_TYPES])
        survey_type = survey_types.get(data['type'], '')
        data['type'] = survey_type
        super(CommuterSurveyLoader, self).create_instance(data)
