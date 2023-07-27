# urls.py в apps
from django.urls import path
from .views import UserGeneratorView, HomePageView

app_name = "base"

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),  # Додайте новий URL для початкової сторінки
    path("generate/", UserGeneratorView.as_view(), name="generate_users"),
]
