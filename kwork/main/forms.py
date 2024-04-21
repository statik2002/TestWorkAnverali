from django.forms import ModelForm, TextInput, CheckboxInput

from main.models import Customer


class LoginForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'password']
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
        }


class RegistrationForm(ModelForm):
    class Meta:
        model = Customer
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
            'is_customer'
        ]
        widgets = {
            'username': TextInput(attrs={'class': 'form-control'}),
            'password': TextInput(attrs={'class': 'form-control'}),
            'first_name': TextInput(attrs={'class': 'form-control'}),
            'last_name': TextInput(attrs={'class': 'form-control'}),
            'is_customer': CheckboxInput(attrs={'class': 'form-check-input'})
        }
        labels = {

        }
