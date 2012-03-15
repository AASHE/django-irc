from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        import doctest
        from rc.resources.apps.scrape import parsers
        doctest.testmod(parsers.operations)
        doctest.testmod(parsers.education)        
        doctest.testmod(parsers.pae)        
