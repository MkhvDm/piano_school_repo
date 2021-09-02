from django.shortcuts import render
from django.http import HttpResponse


def welcome_page(request):
    return HttpResponse("<h1/>WELCOME PAGE<h1>")


def biography(request):
    return HttpResponse("<h1/>BIO<h1>")


def contacts(request):
    return HttpResponse("<h1/>CONTACTS<h1>")