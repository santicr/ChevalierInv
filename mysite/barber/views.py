from django.shortcuts import render, redirect
from django.contrib import messages as m
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import requires_csrf_token
from .forms import BarberForm
from .models import Barber

# Create your views here.
@login_required
def index(req):
    barbers = Barber.objects.all()
    ctx = {'barbers': barbers}
    return render(req, 'barber/barber.html', ctx)

@login_required
@requires_csrf_token
def add_barber(req):
    form = BarberForm()
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

        m.error(req, 'No se pudo registrar el barbero')
        return redirect('main:index')
    return render(req, 'barber/add_barber.html', {'form': form})

@login_required
@requires_csrf_token
def delete_barber(req, id: int):
    if req.method == 'POST':
        barber = Barber.objects.get(id = id)
        barber.delete()
        m.info(req, 'Barbero eliminado correctamente!')
        return redirect('barber:index')