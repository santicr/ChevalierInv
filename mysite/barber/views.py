from django.shortcuts import render, redirect
from django.contrib import messages as m
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import requires_csrf_token
from .forms import BarberForm, ModifyBarberForm
from .models import Barber

# Create your views here.
@login_required
def index(req):
    barbers = Barber.objects.all()
    barber_form = BarberForm()
    modify_barber_form = ModifyBarberForm()
    ctx = {'barbers': barbers, 'barber_form': barber_form, 'modify_barber_form': modify_barber_form}
    return render(req, 'barber/barber.html', ctx)

@login_required
@requires_csrf_token
def add_barber(req):
    if req.method == 'POST':
        data = req.POST
        form = BarberForm(data)

        if form.is_valid():
            name = data['name']
            lastname1 = data['lastname1']
            lastname2 = data['lastname2']
            barber = Barber(name = name, lastname1 = lastname1, lastname2 = lastname2)
            barber.save()
            m.info(req, 'Barbero registrado exitosamente!')
            return redirect('barber:index')

        m.error(req, 'No se pudo registrar el barbero')
        return redirect('main:index')

@login_required
@requires_csrf_token
def modify_barber(req):
    if req.method == 'POST':
        data = req.POST
        id = data['id']
        name = data['name']
        lastname1 = data['lastname1']
        lastname2 = data['lastname2']
        
        try:
            barber = Barber.objects.get(id = id)
        except:
            m.error(req, f'Barbero con id {id} no existe')
            return redirect('barber:index')
        
        barber.name = name
        barber.lastname1 = lastname1
        barber.lastname2 = lastname2
        barber.save()

        m.info(req, 'Barbero modificado exitosamente!')
        return redirect('barber:index')

@login_required
@requires_csrf_token
def delete_barber(req, id: int):
    if req.method == 'POST':
        barber = Barber.objects.get(id = id)
        barber.delete()
        m.info(req, 'Barbero eliminado correctamente!')
        return redirect('barber:index')