from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from datetime import datetime, timedelta, date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from LibraryManagement.models import Book, Material, Device, Container, TempLoan, LoanSubject, Loan


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


@login_required(login_url="/login")
def logout_route(request):
    logout(request)
    return redirect("/")

  
@login_required(login_url="/login")
def borrow_route(request):
    subject_id = request.GET.get('id')
    now = datetime.now()
    loan = TempLoan(date_of_issue=now, expected_return_date=now + timedelta(days=14), borrower=request.user)
    loan.save()
    item = get_object_or_404(LoanSubject, pk=subject_id)
    if not item.is_available():
        return HttpResponseBadRequest()

    if item is not None:
        item.loans.add(loan)
        item.save()

    return redirect('/profile/')


@login_required(login_url="/login")
def return_route(request):
    loan_id = request.GET.get('id')
    loan = get_object_or_404(Loan, pk=loan_id)
    loan.return_date = date.today()
    loan.save()
    return redirect("/profile/")


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

    def _filter_available(query):
        for s in query:
            if s.is_available():
                yield s

    context = {
        "books": _filter_available(books),
        "materials": _filter_available(materials),
        "devices": _filter_available(devices),
        "containers": _filter_available(containers)
    }

    return render(request, 'overview.html', context)


def detail_page(request, id):
    subject = get_object_or_404(LoanSubject, pk=id)
    return render(request, 'detail.html', {"subject": subject})


@login_required(login_url="/login")
def profile_page(request):
    loans = TempLoan.objects.filter(borrower=request.user, return_date__isnull=True)
    return render(request, 'profile.html', {"loans": loans})


@login_required
def print_codes_page(request):
    raw_ids = request.GET.get('ids')
    if raw_ids is None:
        return redirect('/')

    ids = raw_ids.split(',')
    books = [get_object_or_404(Book, pk=id) for id in ids]
    print(books)
    return render(request, 'print_codes.html', {"books": books})
