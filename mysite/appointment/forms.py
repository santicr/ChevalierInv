from django import forms
from barber.models import Barber

class ReserveForm(forms.Form):
    choices = Barber.objects.all()
    choices = [(b, b) for b in choices]
    name = forms.CharField(label = 'Nombre completo', max_length = 100, required = True, widget = forms.TextInput(
        attrs = {'type': 'text', 'class': 'form-control'}
    ))
    lastname1 = forms.CharField(label = 'Apellido paterno', max_length = 100, required = True, widget = forms.TextInput(
        attrs = {'type': 'text', 'class': 'form-control'}
    ))
    lastname2 = forms.CharField(label = 'Apellido materno', max_length = 100, required = True, widget = forms.TextInput(
        attrs = {'type': 'text', 'class': 'form-control'}
    ))
    email = forms.EmailField(label = 'Correo electronico', required = True, widget = forms.EmailInput(
        attrs = {'type': 'email', 'class': 'form-control'}
    ))
    date = forms.DateTimeField(label = 'Fecha para peluquearse', required = True, widget = forms.DateTimeInput(
        attrs = {'type': 'date', 'min': "2023-01-01", 'max': "2023-12-31", 'lang': 'fr-CA'}
    ))
    hour = forms.TimeField(label = 'Selecciona la hora disponible', required = True, widget = forms.TimeInput(
        attrs = {'type': 'time', 'min': '8:00', 'max': '18:00'}
    ))
    barber = forms.ChoiceField(choices = choices, required = True, label = 'Barbero')