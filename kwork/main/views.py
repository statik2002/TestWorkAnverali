from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from main.forms import RegistrationForm, LoginForm


def index(request):

    login_form = LoginForm()
    registration_form = RegistrationForm()

    context = {
        'registration_form': registration_form,
        'login_form': login_form
    }

    return render(request, 'main/index.html', context)


def login_view(request):
    user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    if user is not None:
        login(request, user)
        context = {
            'user': user
        }
        return HttpResponseRedirect(reverse("main:index"))

    else:
        context = {
            'error': 'Неправильный логин или пароль'
        }
        return render(request, 'main/user_login_error.html', context)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("main:index"))


def registration_view(request):

    form = RegistrationForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.password = make_password(user.password)
        user.is_active = True
        user.save()

    return HttpResponseRedirect(reverse("main:index"))
