# rentals/management/commands/list_rental_users.py

from django.core.management.base import BaseCommand
from rentals.models import Rental


class Command(BaseCommand):
    help = 'Cписок пользователей, которые арендовали автомобили'

    def handle(self, *args, **options):
        rental_users = Rental.objects.values_list('user__username', flat=True).distinct()

        self.stdout.write("Те, кто арендовал автомобили")
        for user in rental_users:
            self.stdout.write(self.style.SUCCESS(user))
#список уникальных имен пользователей, которые арендовали автомобили "python manage.py list_rental_users"


