from django.shortcuts import render
from django.http import HttpResponse


def trial(request):
    return HttpResponse("<h1/>Trial lesson<h1>")


def biography(request):
    return HttpResponse("<h1/>BIO<h1>")


def contacts(request):
    return HttpResponse("<h1/>CONTACTS<h1>")


def login(request):
    return render(request, 'main/login.html')