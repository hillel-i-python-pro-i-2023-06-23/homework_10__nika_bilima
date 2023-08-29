import random
import string

from django.shortcuts import render
from django.views import View
from apps.models.user_data import UserData


class HomePageView(View):
    def get(self, request):
        return render(request, "home.html")


class UserGeneratorView(View):
    def generate_unique_string(self, length):
        characters = string.ascii_letters + string.digits
        return "".join(random.choice(characters) for _ in range(length))

    def get(self, request):
        num_users = int(request.GET.get("num_users", 10))
        generated_users = set()
        users_data = []

        while len(users_data) < num_users:
            login = self.generate_unique_string(8)
            email = f"{login}@example.com"
            password = self.generate_unique_string(12)

            if login not in generated_users and email not in generated_users:
                generated_users.add(login)
                generated_users.add(email)
                users_data.append(UserData(login, email, password))

        return render(request, "users_list.html", {"users_data": users_data})
