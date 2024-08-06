from django.core.management.base import BaseCommand
from machines.models import LogisticsBox, Exception

class Command(BaseCommand):
    help = 'Clear the contents of the LogisticsBox and Exception tables'

    def handle(self, *args, **options):
        LogisticsBox.objects.all().delete()
        Exception.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Successfully cleared LogisticsBox and Exception tables'))