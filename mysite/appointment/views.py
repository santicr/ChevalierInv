from django.shortcuts import render, redirect
from .forms import ReserveForm
from datetime import datetime, timedelta, date

# Create your views here.
def reserve(req):
    form = ReserveForm()
    if req.method == 'POST':
        data = req.POST
        form = ReserveForm(data)

        if form.is_valid():
            name = data['name']
            lname1 = data['lastname1']
            lname2 = data['lastname2']
            email = data['email']
            date = data['date']
            hour = data['hour']
            barber = data['barber']

        return redirect('index')
    
    return render(req, 'appointment/reserve.html', {'form': form})