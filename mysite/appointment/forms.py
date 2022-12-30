from django import forms
from barber.models import Barber
from .models import Appointment
from datetime import datetime, timedelta, date

class ReserveForm(forms.Form):
    barber_choices = Barber.objects.all()
    barber_choices = [(b, b) for b in barber_choices]
    first_hour = timedelta(hours = 8, minutes = 30)
    time_choices = [(i, timedelta(hours = 8, minutes = 30) + timedelta(minutes = 30 * i)) for i in range(23)]

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
    date = forms.DateTimeField(label = 'Fecha de reserva', required = True, widget = forms.DateTimeInput(
        attrs = {'type': 'date', 'min': "2023-01-01", 'max': "2023-12-31", 'lang': 'fr-CA'}
    ))
    hour = forms.ChoiceField(choices = time_choices, required = True, label = 'Hora')
    barber = forms.ChoiceField(choices = barber_choices, required = True, label = 'Barbero')
