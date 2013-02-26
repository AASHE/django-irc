from django.core.management.base import BaseCommand, CommandError
from rc.resources.apps.academic_programs.parser import ProgramLoader

class Command(BaseCommand):
    # args = 'whatever'
    help = 'loads data from aashe programs site'

    def handle(self, *args, **options):
        # Load data here
        loader = ProgramLoader()
        loader.save()