from django.urls import path
from . import views

urlpatterns = [
    path("generate-fake-data/", views.generate_fake_data, name="generate_fake_data"),
]
