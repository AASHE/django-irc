from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from rc.cms.process import generate_pages

class Command(BaseCommand):
        
    # option_list = BaseCommand.option_list + (
    #    make_option('--category', action='store', dest='category_name', 
    #                help='Category of models to load'),
    #    make_option('--models', action='store', dest='model_names',
    #                help='Models to load') )

    def handle(self, *args, **options):
        generate_pages()