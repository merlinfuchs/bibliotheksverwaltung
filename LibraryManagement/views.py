import sys

from django.shortcuts import render
from django.contrib.auth import authenticate
from LibraryManagement.models import Device, Container, Book, Author, Material



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

def detail(request, content_type, loansubject_ptr_id):
    content_type_checkup = ['device', 'container', 'book', 'author', 'material']
    content = None
    #TODO Cant find a better solution at the moment
    if content_type in content_type_checkup:
        if content_type == 'device':
            content = Device.objects.get(id=loansubject_ptr_id)
        elif content_type == 'container':
            content = Container.objects.get(id=loansubject_ptr_id)
        elif content_type == 'book':
            content = Book.objects.get(id=loansubject_ptr_id)
        elif content_type == 'author':
            content = Author.objects.get(id=loansubject_ptr_id)
        elif content_type == 'material':
            content = Material.objects.get(id=loansubject_ptr_id)
    return render(request, 'detail.html', content)
