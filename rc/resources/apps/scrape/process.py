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
    some_transforms = set()
    all_transforms = etl.all()

    for model_name in model_names:
        transforms_for_model_name = [ transform for transform in all_transforms
                                      if transform['model'].endswith(model_name) ]
        if transforms_for_model_name:
            for transform in transforms_for_model_name:
                some_transforms.add('\t'.join((transform['model'], 
                                               transform['parser'].__name__)))
        else:
            print(colors.FAIL + 
                  "ERROR: No transforms for model(s) named {0} found".format(model_name))        

    for transform in some_transforms:
        model, parser_name = transform.split('\t')
        process_one([ t for t in all_transforms 
                      if t['model'] == model and t['parser'].__name__ == parser_name ][0])
            
def process_category(category_name):
    transforms = [ transform for transform in etl.all()
                   if transform['model'].startswith(category_name) ]
    if transforms:
        process_some([ model['model'] for model in transforms ])

def process_one(transform):
    loader = create_loader_from_etl(transform)
    parser_name = str(transform['parser']).split('.')[-1][0:-2]
    print "loading {0}, parsed by {1} . . .".format(transform['model'], parser_name)
                      
    try:
        loader.load_all()
    except LoaderException:
        print(colors.FAIL + "ERROR: Unable to load %(model)s using %(loader)s, exception follows . . ." %
              {'model': transform['model'],
               'loader': transform['loader']})
        print(colors.ENDC)        
