from django.core.management.base import BaseCommand
from faker import Faker
from apps.contact_manager.models import Contact, ContactData, Group, ContactDataType
import random
import string

fake = Faker()


class Command(BaseCommand):
    help = "Populate database with fake data"

    def handle(self, *args, **options):
        self.populate_data()

    def populate_data(self):
        group_names = ["Family", "Friends", "Colleagues", "Acquaintances", "Clients", "Vacations", "Camp"]

        initial_types = ["telegram", "viber", "instagram", "steam", "linkedin", "other"]
        for type_name in initial_types:
            ContactDataType.objects.get_or_create(name=type_name)

        contact_data_types = ContactDataType.objects.all()

        for _ in range(50):
            contact = Contact.objects.create(name=fake.name(), birthday=fake.date_of_birth())

            group_name = random.choice(group_names)

            group, created = Group.objects.get_or_create(name=group_name)
            contact.groups.add(group)

            contact_data_type = random.choice(contact_data_types)

            value = self.generate_fake_data(contact_data_type)

            ContactData.objects.create(contact=contact, contact_type=contact_data_type, value=value)

    def generate_fake_data(self, contact_data_type):
        if contact_data_type.name == "viber":
            return "+380" + "".join(random.choices(string.digits, k=9))
        elif contact_data_type.name == "steam":
            return fake.email()
        elif contact_data_type.name == "instagram" or contact_data_type.name == "telegram":
            return "@" + fake.user_name()
        elif contact_data_type.name == "linkedin":
            return fake.user_name()
        else:
            return fake.word()
