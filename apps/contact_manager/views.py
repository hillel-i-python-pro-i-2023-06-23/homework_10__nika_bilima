from django.shortcuts import redirect
from django.core.management import call_command


def generate_fake_data(request):
    call_command("populate_data")
    return redirect("base")
