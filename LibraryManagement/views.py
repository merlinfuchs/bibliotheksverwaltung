from django.shortcuts import render, redirect
from LibraryManagement.models import Book, Material, Device, Container
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if not request.POST.get("save"):
                request.session.set_expiry(60 * 60)

            return redirect("/")
        else:
            return render(request, 'login.html', {"failed": True})

    return render(request, 'login.html', {})


def logout_route(request):
    logout(request)
    return redirect("/")


def overview_page(request):
    search = request.GET.get("search", "")
    base_filter = Q(name__icontains=search) | Q(description__icontains=search)

    books = Book.objects.filter(
        base_filter | Q(subject__icontains=search) |
        Q(author__first_name__icontains=search) |
        Q(author__last_name__icontains=search)
    )
    materials = Material.objects.filter(base_filter)
    devices = Device.objects.filter(base_filter | Q(device_type__icontains=search))
    containers = Container.objects.filter(base_filter)

    context = {
        "books": books,
        "materials": materials,
        "devices": devices,
        "containers": containers
    }

    return render(request, 'overview.html', context)


def profile_page(request):
    return render(request, 'profile.html', {})
