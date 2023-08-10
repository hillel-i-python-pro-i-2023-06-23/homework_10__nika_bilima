from django.urls import path
from . import views

app_name = "contacts"

urlpatterns = [
    path("", views.contact_list, name="contact_list"),
    path("generate/", views.generate_contacts, name="generate_contacts"),
    path("delete/", views.delete_contacts, name="delete_contacts"),
    path("create/", views.contact_create, name="contact_create"),
    path("detail/<int:pk>", views.contact_detail, name="contact_detail"),
    path("update/<int:pk>", views.contact_update, name="contact_update"),
    path("delete/<int:pk>", views.contact_delete, name="contact_delete"),
    path("list_crud/", views.contact_list_crud, name="contact_list_crud"),  # Додайте цей маршрут
]
