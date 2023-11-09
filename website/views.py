from django.shortcuts import render


def home(request):
    context = {
        "title": "Home Page",
        "header": "Selamat Datang!",
    }

    return render(request, "home.html", context)
