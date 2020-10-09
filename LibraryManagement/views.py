from django.shortcuts import render


def login(request):
    return render(request, 'login.html', {})


def overview(request):
    return render(request, 'overview.html', {
        "objects": [
            {
                "name": "Buch 1",
                "category": "Buch",
                "subject": "Mathe",
                "author": "Hans Peter Wurst",
                "description": "ich bin ein olles test buch"
            },
            {
                "name": "Buch 2",
                "category": "Buch",
                "subject": "Deutsch",
                "author": "jösfnjköhsf",
                "description": "kann nix will nix tut nix"
            },
            {
                "name": "Buch 2",
                "category": "Buch",
                "subject": "Deutsch",
                "author": "jösfnjköhsf",
                "description": "kann nix will nix tut nix"
            },
            {
                "name": "Buch 2",
                "category": "Buch",
                "subject": "Deutsch",
                "author": "jösfnjköhsf",
                "description": "kann nix will nix tut nix"
            },
            {
                "name": "Buch 2",
                "category": "Buch",
                "subject": "Deutsch",
                "author": "jösfnjköhsf",
                "description": "kann nix will nix tut nix"
            },
            {
                "name": "Buch 2",
                "category": "Buch",
                "subject": "Deutsch",
                "author": "jösfnjköhsf",
                "description": "kann nix will nix tut nix"
            },
            {
                "name": "Buch 2",
                "category": "Buch",
                "subject": "Deutsch",
                "author": "jösfnjköhsf",
                "description": "kann nix will nix tut nix"
            },
            {
                "name": "Buch 2",
                "category": "Buch",
                "subject": "Deutsch",
                "author": "jösfnjköhsf",
                "description": "kann nix will nix tut nix"
            },
            {
                "name": "Buch 2",
                "category": "Buch",
                "subject": "Deutsch",
                "author": "jösfnjköhsf",
                "description": "kann nix will nix tut nix"
            },
            {
                "name": "Buch 2",
                "category": "Buch",
                "subject": "Deutsch",
                "author": "jösfnjköhsf",
                "description": "kann nix will nix tut nix"
            },
            {
                "name": "Buch 2",
                "category": "Buch",
                "subject": "Deutsch",
                "author": "jösfnjköhsf",
                "description": "kann nix will nix tut nix"
            },
            {
                "name": "Buch 2",
                "category": "Buch",
                "subject": "Deutsch",
                "author": "jösfnjköhsf",
                "description": "kann nix will nix tut nix"
            },
            {
                "name": "Buch 2",
                "category": "Buch",
                "subject": "Deutsch",
                "author": "jösfnjköhsf",
                "description": "kann nix will nix tut nix"
            },
            {
                "name": "Buch 2",
                "category": "Buch",
                "subject": "Deutsch",
                "author": "jösfnjköhsf",
                "description": "kann nix will nix tut nix"
            },
            {
                "name": "Buch 2",
                "category": "Buch",
                "subject": "Deutsch",
                "author": "jösfnjköhsf",
                "description": "kann nix will nix tut nix"
            },
            {
                "name": "Buch 2",
                "category": "Buch",
                "subject": "Deutsch",
                "author": "jösfnjköhsf",
                "description": "kann nix will nix tut nix"
            },
            {
                "name": "Buch 2",
                "category": "Buch",
                "subject": "Deutsch",
                "author": "jösfnjköhsf",
                "description": "kann nix will nix tut nix"
            },
            {
                "name": "Laptopwagen",
                "device": "Laptops",
                "category": "Container",
                "description": "Wagen mit Laptops"
            }
        ]
    })


def profile(request):
    return render(request, 'profile.html', {})
