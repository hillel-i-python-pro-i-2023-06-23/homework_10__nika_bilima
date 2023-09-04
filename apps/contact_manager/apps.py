from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class ContactsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.contact_manager"

    @receiver(post_migrate)
    def populate_data(sender, **kwargs):
        from .models import Contact

        if not Contact.objects.exists():
            from django.core.management import call_command

            call_command("populate_data")
