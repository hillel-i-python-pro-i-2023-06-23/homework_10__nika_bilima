from django.shortcuts import render
from .models import Contact
from .management.commands.generate_contacts import Command as GenerateCommand
from .management.commands.delete_contacts import Command as DeleteCommand


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contact_list.html", {"contacts": contacts})


def generate_contacts(request):
    message = None
    if request.method == "POST":
        total = int(request.POST.get("total", 0))
        GenerateCommand().handle(total=total)
        message = f"Successfully generated {total} contacts."

    return render(request, "generate_contacts.html", {"message": message})


def delete_contacts(request):
    message = None
    if request.method == "POST":
        DeleteCommand().handle()
        message = "All contacts have been deleted."

    return render(request, "delete_contacts.html", {"message": message})
