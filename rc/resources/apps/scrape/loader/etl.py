# ETLRegistry - simple ETL registration class
#
# Associates a page parser, a loader class, and a Django model class

from collections import OrderedDict

class ETLRegistry(object):
    '''
    A registry to associate parsers with their loader and
    model. Supports kwargs to be passed to the loader at runtime.
    '''
    def __init__(self):
        self._registry = OrderedDict()
    def register(self, parser, loader, model_or_string, **kwargs):
        etl_dict = {'parser': parser,
                    'loader': loader,
                    'model': model_or_string,
                    'kwargs': kwargs}
        self._registry.update({parser: etl_dict})
    def all(self):
        return self._registry.values()
    def get_by_parser(self, parser):
        return self._registry.get(parser)
    def get(self, parser):
        return self.get_by_parser(parser)
etl = ETLRegistry()
