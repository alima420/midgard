import csv
from django.core.management.base import BaseCommand
from machines.models import ProductBox
from datetime import datetime

class Command(BaseCommand):
    help = 'Import ProductBox data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to be imported')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Strip whitespace from keys and values
                row = {key.strip(): value.strip() for key, value in row.items()}
                
                try:
                    ProductBox.objects.create(
                        logistics_box_id=row['LogisticsBoxId'],
                        logistics_box_timestamp=datetime.strptime(row['LogisticsBoxTimeStamp'], '%Y-%m-%d %H:%M:%S'),
                        number_units=row['NumberUnits'],
                        article_number=row['ArticleNumber'],
                        product_box_id=row['ProductBoxId'],
                        product_serial=row['ProductSerial'],
                        device_creation_timestamp=datetime.strptime(row['DeviceCreationTimeStamp'], '%Y-%m-%d %H:%M:%S'),
                        device_remarks=row['DeviceRemarks']
                    )
                except KeyError as e:
                    self.stdout.write(self.style.ERROR(f'Missing key in row: {e}. Row keys: {row.keys()}'))
                    continue

        self.stdout.write(self.style.SUCCESS('Data imported successfully'))
