from django.shortcuts import render, redirect
from .forms import ReserveForm
from appointment.models import Appointment
from datetime import datetime, timedelta, date, time

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
            reserve_date = data['date'].split('-')
            reserve_date = date(int(reserve_date[0]), int(reserve_date[1]), int(reserve_date[2]))
            barber = int(data['barber'].strip().split()[-1])
            appointments = Appointment.objects.filter(barber = barber).filter(date = reserve_date)
            time_choices = []

            for i in range(23):
                t = timedelta(hours = 8, minutes = 30) + timedelta(minutes = 30 * i)
                new_time = time(t.seconds // 3600, (t.seconds // 60) % 60, 0)
                flag = False
                for appointment in appointments:
                    if appointment.hour == new_time:
                        flag = True
                if not flag:
                    time_choices.append(new_time)

        return redirect('index')
    
    return render(req, 'appointment/reserve.html', {'form': form})