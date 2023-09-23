from django.contrib import admin
from .models import Contact, Group, ContactDataType, ContactData
from django.db.models import Count


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "birthday", "get_groups", "get_contact_data_by_type", "num_contact_data")

    def get_queryset(self, request):
        queryset = super().get_queryset(request).annotate(num_contact_data=Count("contactdata"))
        return queryset

    def num_contact_data(self, obj):
        return obj.num_contact_data

    num_contact_data.short_description = "Contact Data Count"

    def changelist_view(self, request, extra_context=None):
        total_contact_data_types = ContactDataType.objects.annotate(num_contact_data=Count("contactdata")).count()

        extra_context = extra_context or {}
        extra_context["title"] = f"Total Contact Data Types: {total_contact_data_types}"
        return super().changelist_view(request, extra_context=extra_context)

    def get_contact_data_by_type(self, obj):
        contact_types = ContactDataType.objects.all()
        data = []
        for contact_type in contact_types:
            contact_data = obj.contactdata_set.filter(contact_type=contact_type).first()
            if contact_data:
                data.append(f"{contact_type.name}: {contact_data.value}")
        return ", ".join(data)

    get_contact_data_by_type.short_description = "Contact Data by Type"

    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])

    get_groups.short_description = "Groups"

    def get_contact_data(self, obj):
        data = []
        for contact_data in obj.contactdata_set.all():
            data.append(f"{contact_data.contact_type.name}: {contact_data.value}")
        return ", ".join(data)

    get_contact_data.short_description = "Contact Data"


class ContactInline(admin.TabularInline):
    model = Contact.groups.through
    extra = 0
    verbose_name = "Contact"
    verbose_name_plural = "Contacts"


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("name", "get_contacts")

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("contacts")

    def get_contacts(self, obj):
        return ", ".join([contact.name for contact in obj.get_contacts()])

    get_contacts.short_description = "Contacts"

    inlines = [ContactInline]


@admin.register(ContactData)
class ContactDataAdmin(admin.ModelAdmin):
    list_display = ("contact", "contact_type", "value")


class ContactDataInline(admin.TabularInline):
    model = ContactData
    extra = 0


@admin.register(ContactDataType)
class ContactDataTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "validation_regex", "total_contacts_with_type")

    def total_contacts_with_type(self, obj):
        return Contact.objects.filter(contactdata__contact_type=obj).count()

    total_contacts_with_type.short_description = "Total Contacts with Type"
    inlines = [ContactDataInline]
