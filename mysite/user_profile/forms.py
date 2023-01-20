from django import forms
from django.contrib.auth.forms import AuthenticationForm

class NewAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario', required=True, widget = forms.TextInput(
        attrs={'class': 'form-control'}
    ))
    password = forms.CharField(label='Contraseña', required=True, widget = forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))