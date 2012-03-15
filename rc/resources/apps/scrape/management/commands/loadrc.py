from django.core.management.base import BaseCommand, CommandError

from rc.resources.apps.scrape.process import process_all, process_some

class Command(BaseCommand):
    def handle(self, *args, **options):
        if args:
            process_some(args)
        else:
            process_all()
        
        
