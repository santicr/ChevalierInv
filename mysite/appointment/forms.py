from django import forms

class ReserveForm(forms.Form):
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