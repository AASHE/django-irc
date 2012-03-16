from optparse import make_option

from django.core.management.base import BaseCommand, CommandError

from rc.resources.apps.scrape.process import process_all, process_some, process_category


class Command(BaseCommand):
        
    option_list = BaseCommand.option_list + (
        make_option('--category', action='store', dest='category_name', 
                    help='Category of models to load'),
        make_option('--models', action='store', dest='model_names',
                    help='Models to load') )

    def handle(self, *args, **options):
        if args:
            arg_string = ' '.join(args)
            options['model_names'] = (' '.join((options['model_names'], arg_string)) 
                                      if options['model_names'] 
                                      else arg_string)
        if options['model_names'] or options['category_name']:
            if options['model_names']:
                process_some(options['model_names'].split())
            if options['category_name']:
                process_category(options['category_name'])
        else:
            process_all()
        
        
