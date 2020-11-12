from django.shortcuts import render
from LibraryManagement.models import Book, Material, Device, Container
from itertools import chain


def login(request):
    return render(request, 'login.html', {})


def overview(request):
    name_filter = {}
    name = request.GET.get('name_field')
    if name:
        name_filter['name'] = name

    book_filter = {}
    subject = request.GET.get('book_subject')
    if subject:
        book_filter['subject'] = subject

    device_filter = {}
    device_type = request.GET.get('type_of_device')
    if device_type:
        device_filter['device_type'] = device_type

    books = Book.objects.filter(**name_filter, **book_filter)
    materials = Material.objects.filter(**name_filter)
    devices = Device.objects.filter(**name_filter, **device_filter)
    containers = Container.objects.filter(**name_filter)

    context = {
        "books": books,
        "materials": materials,
        "devices": devices,
        "containers": containers
    }

    return render(request, 'overview.html', context)


def profile(request):
    return render(request, 'profile.html', {})
