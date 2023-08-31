from faker import Faker
from django.core.management.base import BaseCommand
from apps.contacts.models import Contact


class Command(BaseCommand):
    help = "Generate random contacts"

    def add_arguments(self, parser):
        parser.add_argument("total", type=int, nargs="?", help="Indicates the number of contacts to be generated")

    def handle(self, *args, **options):
        fake = Faker()
        total = options["total"]
        for i in range(total):
            name = fake.name()
            phone = fake.phone_number()
            Contact.objects.create(name=name, phone=phone)
        self.stdout.write(self.style.SUCCESS(f"Successfully generated {total} contacts"))
