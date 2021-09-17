from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User


def account(request):
    print(request)
    user = request.user
    print(user)
    username = user.get_username()
    print('debug:', username)
    return render(request, 'account/account.html', {'username': username})


def login_v(request):
    if request.method == 'GET':
        # if not user.is_authenticated:
            # redirect to account
        login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('account:account')
    return render(request, 'account/login.html', {'login_form': login_form})


def sign_up(request):
    if request.method == 'GET':
        sign_up_form = UserCreationForm()
    else:
        sign_up_form = UserCreationForm(request.POST)
        if sign_up_form.is_valid():
            user = sign_up_form.save()
            login(request, user)
        # return HttpResponse('sign_up done')
        return redirect('account:account')
    return render(request, 'account/sign_up.html', {'sign_up_form': sign_up_form})


def logout_v(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

