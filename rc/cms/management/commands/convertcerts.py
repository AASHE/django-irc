from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from rc.resources.apps.operations.models import *


class Command(BaseCommand):

    
    def handle(self, *args, **options):
        certs = (( 'PL', 'AP'),
                ('GL' , 'BG'),
                ('SL' , 'CS'),
                ('BZ' , 'DB'),
                ('CR' , 'EC'),
                ('NC' , 'GN'),
                )
        certs = dict(certs)
        for before, after in certs.items():
            buildings = CampusGreenBuilding.objects.filter(certification=('%s' % before))
            for building in buildings:
                building.certification = after
                building.save()