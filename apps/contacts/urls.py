from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.contact_list, name="contact_list"),
    path("generate/", views.generate_contacts, name="generate_contacts"),
    path("delete/", views.delete_contacts, name="delete_contacts"),
]
