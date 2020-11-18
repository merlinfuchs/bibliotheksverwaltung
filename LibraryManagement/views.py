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
            device = Device.objects.get(id=loansubject_ptr_id)
            content = {'device_type':device.device_type, 'name':device.name, 'description':device.description}
            return render(request, 'detail/detail_device.html', content)
        elif content_type == 'container':
            container = Container.objects.get(id=loansubject_ptr_id)
            content = {'name':container.name, 'description':container.description}
            return render(request, 'detail/detail_container.html', content)
        elif content_type == 'book':
            book = Book.objects.get(id=loansubject_ptr_id)
            content = {'name':book.name, 'isbn':book.isbn, 'subject':book.subject, 'description':book.description}
            return render(request, 'detail/detail_book.html', content)
        elif content_type == 'author':
            author = Author.objects.get(id=loansubject_ptr_id)
            content = {'first_name':author.first_name, 'last_name':author.last_name}
            return render(request, 'detail/detail_author.html', content)
        elif content_type == 'material':
            material = Material.objects.get(id=loansubject_ptr_id)
            content = {'name':material.name, 'description':material.description}
            return render(request, 'detail/detail_material.html', content)
        #TODO render a 404 not found template
    return render(request, 'detail/detail_device.html', content)
