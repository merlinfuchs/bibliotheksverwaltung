from django.shortcuts import render, redirect
from LibraryManagement.models import Book, Material, Device, Container
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
import datetime
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from LibraryManagement.models import Book, Material, Device, Container, TempLoan
from itertools import chain
from django.contrib.auth import authenticate


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

  
@login_required
def borrow(request):
    id = request.GET.get('id')
    type = request.GET.get('type')  # Types: book, material, device, container
    loan = TempLoan(date_of_issue=datetime.timezone.now(), borrower=request.user)
    item = None
    if type == 'book':
        item = Book.objects.get(pk=id)
    elif type == 'material':
        item = Material.objects.get(pk=id)
    elif type == 'device':
        item = Device.objects.get(pk=id)
    elif type == 'container':
        item = Container.objects.get(pk=id)

    if item is not None:
        item.loan_object.add(loan)
        loan.save()
    return redirect('/overview/')


def overview(request):
    name_filter = {}
    name = request.GET.get('name_field')
    if name:
        name_filter['name'] = name


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


def admin_overview(request):
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

    loan_filter = {}
    subject = request.GET.get('loan_object')
    if subject:
        loan_filter['subject'] = subject

    books = Book.objects.filter(**name_filter, **book_filter, **loan_filter)
    materials = Material.objects.filter(**name_filter, **loan_filter)
    devices = Device.objects.filter(**name_filter, **device_filter, **loan_filter)
    containers = Container.objects.filter(**name_filter, **loan_filter)

    context = {
        "books": books,
        "materials": materials,
        "devices": devices,
        "containers": containers
    }

    return render(request, 'admin_overview.html', context)
