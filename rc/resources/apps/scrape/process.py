from django.db.models import get_model
from rc.resources.apps.scrape.loader.registry import etl


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
        loader = create_loader_from_etl(transform)
        loader.load_all()
