from django.db.models import get_model
from rc.resources.apps.scrape.loader.registry import etl
from rc.resources.apps.scrape.loader import LoaderException


class colors:
    FAIL = '\033[91m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'

def get_model_class(model_or_string):
    if isinstance(model_or_string, basestring):
        return get_model(*model_or_string.split('.'))
    else:
        return model_or_string

def create_loader_from_etl(transform):
    parser_class, loader_class = transform['parser'], transform['loader']
    model = get_model_class(transform['model'])
    kwargs = transform.get('kwargs', {})
    return loader_class(parser_class, model, **kwargs)

def process_all():
    for transform in etl.all():
        process_one(transform)

def process_some(model_names):
    for model_name in model_names:
        try:
            transform = [ transform for transform in etl.all() 
                          if transform['model'].endswith(model_name) ][0]
        except IndexError:
            raise Exception("No model named {0} found".format(model_name))
        process_one(transform)

def process_one(transform):
    loader = create_loader_from_etl(transform)
    print "loading {0} . . .".format(transform['model'])
    try:
        loader.load_all()
    except LoaderException:
        print(colors.FAIL + "ERROR: Unable to load %(model)s using %(loader)s, exception follows . . ." %
              {'model': transform['model'],
               'loader': transform['loader']})
        print(colors.ENDC)        
