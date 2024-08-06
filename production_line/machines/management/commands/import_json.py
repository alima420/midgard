import json
import os
from django.core.management.base import BaseCommand
from machines.models import LogisticsBox, Exception

class Command(BaseCommand):
    help = 'Import JSON data into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file_path = kwargs['json_file']
        
        if not os.path.isfile(json_file_path):
            self.stderr.write(self.style.ERROR('File does not exist'))
            return
        
        with open(json_file_path, 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                self.stderr.write(self.style.ERROR(f'Error decoding JSON: {e}'))
                return

        for box_data in data:
            try:
                box, created = LogisticsBox.objects.get_or_create(
                    logistics_box_id=box_data.get('logistics_box_id'),
                    defaults={'details': box_data.get('details')}
                )
                
                for ex_data in box_data.get('exceptions', []):
                    Exception.objects.create(
                        logistics_box=box,
                        serial_number=ex_data.get('serial_number'),
                        details=ex_data.get('details')
                    )
            except Exception as e:
                self.stderr.write(self.style.ERROR(f'Error processing data: {e}'))
                continue

        self.stdout.write(self.style.SUCCESS('Successfully imported JSON data.'))
