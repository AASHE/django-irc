from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        from rc.resources.apps.scrape.process import process_all
        process_all()
        
        
