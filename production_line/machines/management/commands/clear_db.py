from django.core.management.base import BaseCommand
from machines.models import ProductBox

class Command(BaseCommand):
    help = 'Delete all records from the ProductBox table'

    def handle(self, *args, **kwargs):
        # Confirm the deletion action with the user
        confirm = input("Are you sure you want to delete all records from the ProductBox table? Type 'yes' to continue: ")

        if confirm.lower() == 'yes':
            # Perform the deletion
            count, _ = ProductBox.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted {count} records from the ProductBox table'))
        else:
            self.stdout.write(self.style.ERROR('Operation cancelled'))
