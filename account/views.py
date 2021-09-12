from django.shortcuts import render, redirect, get_object_or_404


def account(request):
    return render(request, 'account/account.html')


def login(request):
    return render(request, 'account/login.html')


def registration(request):
    return render(request, 'account/registration.html')