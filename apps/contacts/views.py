from django.shortcuts import render, redirect
from .models import Contact
from .management.commands.generate_contacts import Command as GenerateCommand
from .management.commands.delete_contacts import Command as DeleteCommand
from .forms import ContactForm


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


def contact_create(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contacts:contact_list")  # Повернення до списку контактів
    else:
        form = ContactForm()
    return render(request, "contact_form.html", {"form": form})


def contact_detail(request, pk):
    contact = Contact.objects.get(pk=pk)
    return render(request, "contact_detail.html", {"contact": contact})


def contact_update(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contacts:contact_list")
    else:
        form = ContactForm(instance=contact)
    return render(request, "contact_form.html", {"form": form, "pk": pk})


def contact_delete(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == "POST":
        contact.delete()
        return redirect("contacts:contact_list")
    return render(request, "contact_confirm_delete.html", {"contact": contact})


def contact_list_crud(request):
    contacts = Contact.objects.all()
    return render(request, "contact_list_crud.html", {"contacts": contacts})
