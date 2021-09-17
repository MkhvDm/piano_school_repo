from django.shortcuts import render
from django.http import HttpResponse


def trial(request):
    return render(request, 'main/trial.html')


def biography(request):
    return render(request, 'main/bio.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def login(request):
    return render(request, 'main/login.html')
