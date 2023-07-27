from django.urls import path
from .views import UserGeneratorView

app_name = "base"

urlpatterns = [path("", UserGeneratorView.as_view(), name="generate_users")]
