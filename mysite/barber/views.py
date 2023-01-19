from django.shortcuts import render, redirect
from .forms import BarberForm
from .models import Barber
from django.contrib import messages as m

# Create your views here.
def add_barber(req):
    form = BarberForm()
    if req.user.is_authenticated:
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
            return redirect('index')
        return render(req, 'barber/barber.html', {'form': form})