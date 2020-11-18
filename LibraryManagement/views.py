from django.shortcuts import render
from django.contrib.auth import authenticate
from LibraryManagement.models import Loan, LoanSubject



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print('User', username, 'Logged in')
            # TODO Create Session
        else:
            print('Authentication failed for User:', username)
    return render(request, 'login.html', {})


def overview(request):
    return render(request, 'overview.html', {})


def profile(request):
    return render(request, 'profile.html', {})

def detail(request, loansubject_id):

    return render(request, 'detail.html', {})
