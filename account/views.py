from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.views.generic import View


def account(request):
    user = request.user
    print(user)
    print(type(user))
    username = user.get_username()
    print('debug:', username)
    print(user.pk)
    # return render(request, 'account/account.html', {'username': username})
    return render(request, 'account/account.html', {'user': user})


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
            return redirect('account:account')
    return render(request, 'account/login.html', {'login_form': login_form})


def logout_v(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def settings(request):

    return redirect('home')


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
            return redirect('account:account')


