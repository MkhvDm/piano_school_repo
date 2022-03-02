from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.views.generic import View

from account.forms import ChangeLastName


def account(request):
    user = request.user
    print(user)
    return render(request, 'account/account.html', {'user': user})


def sign_up(request):
    if request.method == 'GET':
        sign_up_form = UserCreationForm()
        print('sign_up form...')
    else:
        sign_up_form = UserCreationForm(request.POST)
        print('form valid? -', sign_up_form.is_valid())
        if sign_up_form.is_valid():
            user = sign_up_form.save()
            print('user register!')
            login(request, user)
            print('user auth!')
            return redirect('account:account')
        else:
            return redirect('account:sign_up')  # todo on front

    return render(request, 'account/sign_up.html', {'sign_up_form': sign_up_form})


def login_v(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('account:account')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('timepad:timepad_default')
    return render(request, 'account/login.html', {'login_form': login_form})


def logout_v(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def settings(request):
    if request.method == 'POST' and request.user.is_authenticated:
        user = request.user
        print(request.POST)
        if 'new_first_name' in request.POST:
            new_first_name = request.POST['new_first_name']
            user.first_name = new_first_name
            user.save()
        if 'new_last_name' in request.POST:
            new_last_name = request.POST['new_last_name']
            user.last_name = new_last_name
            user.save()
    return redirect('account:account')


class LoginView(View):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('account:account')
        else:
            login_form = self.form_class()
            return render(request, self.template_name, {'login_form': login_form})

    def post(self, request, *args, **kwargs):
        login_form = self.form_class(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('timepad:timepad_default')


