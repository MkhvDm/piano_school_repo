from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth.models import User


def account(request):
    print(request)
    user = request.user
    print(user)
    username = user.get_username()
    print('debug:', username)
    return render(request, 'account/account.html', {'username': username})


def login(request):
    if request.method == 'GET':
        # if not user.is_authenticated:
            # redirect to account
        login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            return redirect('account')
    return render(request, 'account/login.html', {'login_form': login_form})


def sign_up(request):
    if request.method == 'GET':
        sign_up_form = UserCreationForm()
    else:
        sign_up_form = UserCreationForm(request.POST)
        if sign_up_form.is_valid():
            sign_up_form.save()
        # return HttpResponse('sign_up done')
        return redirect('account')
    return render(request, 'account/sign_up.html', {'sign_up_form': sign_up_form})

