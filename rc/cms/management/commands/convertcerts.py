from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from rc.resources.apps.operations.models import *


class Command(BaseCommand):
    
    def handle(self, *args, **options):

        buildings = CampusGreenBuilding.objects.filter(certification='LEED Platinum')

        for building in buildings:
            building.certification = "PL"
            building.save()
    
        buildings = CampusGreenBuilding.objects.filter(certification='LEED Gold')

        for building in buildings:
            building.certification = "GL"
            building.save()

        buildings = CampusGreenBuilding.objects.filter(certification='LEED Silver')

        for building in buildings:
            building.certification = "SL"
            building.save()

        buildings = CampusGreenBuilding.objects.filter(certification='LEED Bronze')

        for building in buildings:
            building.certification = "BZ"
            building.save()

        buildings = CampusGreenBuilding.objects.filter(certification='LEED Certified')

        for building in buildings:
            building.certification = "CR"
            building.save()

        buildings = CampusGreenBuilding.objects.filter(certification='not certified')

        for building in buildings:
            building.certification = "NC"
            building.save()