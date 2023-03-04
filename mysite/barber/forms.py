from django import forms

class BarberForm(forms.Form):
    name = forms.CharField(max_length = 100, label = 'Nombre', widget = forms.TextInput(
        attrs = {'class': 'form-control'}
    ))
    lastname1 = forms.CharField(max_length = 100, label = 'Apellido paterno', widget = forms.TextInput(
        attrs = {'class': 'form-control'}
    ))
    lastname2 = forms.CharField(max_length = 100, label = 'Apellido materno', widget = forms.TextInput(
        attrs = {'class': 'form-control'}
    ))

class ModifyBarberForm(forms.Form):
    id = forms.IntegerField(label = 'Id', widget = forms.TextInput(
        attrs = {'class': 'form-control'}
    ))
    name = forms.CharField(max_length = 100, label = 'Nombre', widget = forms.TextInput(
        attrs = {'class': 'form-control'}
    ))
    lastname1 = forms.CharField(max_length = 100, label = 'Apellido paterno', widget = forms.TextInput(
        attrs = {'class': 'form-control'}
    ))
    lastname2 = forms.CharField(max_length = 100, label = 'Apellido materno', widget = forms.TextInput(
        attrs = {'class': 'form-control'}
    ))