from django.contrib.auth import forms
from django.forms import ModelForm

from main.models import Customer


class LoginForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'password']


class RegistrationForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'first_name', 'last_name', 'password', 'is_customer']
