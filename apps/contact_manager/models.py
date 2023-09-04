import re
from django.core.exceptions import ValidationError
from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_contacts(self):
        return self.contacts.all()


class Contact(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(null=True, blank=True)
    groups = models.ManyToManyField("Group", related_name="contacts")

    def __str__(self):
        return self.name


class ContactDataType(models.Model):
    name = models.CharField(max_length=100)
    validation_regex = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_contacts(self):
        return Contact.objects.filter(contactdata__contact_type=self)


class ContactData(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    contact_type = models.ForeignKey(ContactDataType, on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
    nickname_or_phone = models.CharField(max_length=100)

    def clean(self):
        super().clean()
        if not re.match(self.contact_type.validation_regex, self.value):
            raise ValidationError(f"Invalid data format for type {self.contact_type.name}")
