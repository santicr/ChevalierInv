from django import forms
from barber.models import Barber
from .models import Appointment
from datetime import datetime, timedelta, date

class ReserveForm(forms.Form):
    def convert(time):
        if time >= 1 and time <= 9:
            return str('0' + str(time))
        return str(time)

    barber_choices = Barber.objects.all()
    barber_choices = [(b.id, b) for b in barber_choices]
    start_time = str(datetime.now().year) + '-' + str(convert(datetime.now().month)) + '-' + str(convert(datetime.now().day))
    final_time = str(datetime.now().year + 1) + '-' + str(convert(datetime.now().month)) + '-' + str(convert(datetime.now().day))

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
        attrs = {'type': 'date', 'min': start_time, 'max': final_time, 'lang': 'fr-CA', 'value': start_time}
    ))
    barber = forms.ChoiceField(choices = barber_choices, required = True, label = 'Barbero')

class ReserveHourForm(forms.Form):
    hour = forms.ChoiceField(choices = [], required = True, label = 'Hora')