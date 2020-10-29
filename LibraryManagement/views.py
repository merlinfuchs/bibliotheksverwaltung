from django.shortcuts import render
from LibraryManagement.models import Book, Material, Device, Container


def login(request):
    return render(request, 'login.html', {})


def overview(request):
    books = Book.objects.all()
    materials = Material.objects.all()
    devices = Device.objects.all()
    containers = Container.objects.all()

    return render(request, 'overview.html', {
        "books": books,
        "materials": materials,
        "devices": devices,
        "containers": containers
    })


def profile(request):
    return render(request, 'profile.html', {})
