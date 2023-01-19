from django import forms

class BarberForm(forms.Form):
    name = forms.CharField(max_length = 100, label = 'Nombre')
    lastname1 = forms.CharField(max_length = 100, label = 'Apellido paterno')
    lastname2 = forms.CharField(max_length = 100, label = 'Apellido materno')