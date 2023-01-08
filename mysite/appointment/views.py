from django.shortcuts import render, redirect
from .forms import ReserveForm
from appointment.models import Appointment
from datetime import datetime, timedelta, time
from barber.models import Barber

# Create your views here.
def convert(date: datetime):
    m = str(date.month)
    d = str(date.day)
    if date.month >= 1 and date.month <= 9:
        m = f'0{date.month}'
    if date.day >= 1 and date.day <= 9:
        d = f'0{date.day}'
    return str(date.year) + m + d

def reserve(req, barber_id):
    if req.method == 'POST':
        form = ReserveForm()
        date = req.POST['appointment_date']
        date = list(map(int, date.split('-')))
        date = datetime(date[0], date[1], date[2])
        appointments = Appointment.objects.filter(barber = barber_id).filter(date = date)
        time_choices = []

        for i in range(23):
            t = timedelta(hours = 8, minutes = 30) + timedelta(minutes = 30 * i)
            new_time = time(t.seconds // 3600, (t.seconds // 60) % 60, 0)
            flag = False
            for appointment in appointments:
                if appointment.hour == new_time:
                    flag = True
            if not flag:
                time_choices.append((i, new_time))

        return render(req, 'appointment/reserve.html', {'time_choices': time_choices, 'form': form, 'barber_id': barber_id, 'date': convert(date)})

def get_hour(value):
    new_time = None
    for i in range(value + 1):
        t = timedelta(hours = 8, minutes = 30) + timedelta(minutes = 30 * i)
        new_time = time(t.seconds // 3600, (t.seconds // 60) % 60, 0)
    return new_time

def confirm_reserve(req, barber_id: int, date: str):
    if req.method == 'POST':
        data = req.POST
        form = ReserveForm(data)
        if form.is_valid():
            barber = Barber.objects.get(id = barber_id)
            date = datetime(int(date[0:4]), int(date[4:6]), int(date[6:8]))
            hour = get_hour(int(data['appointment_time']))
            name = data['name']
            lname1 = data['lastname1']
            lname2 = data['lastname2']
            email = data['email']
            new_appointment = Appointment(name = name, barber = barber, date = date, hour = hour, lastname1 = lname1, lastname2 = lname2, email = email)
            new_appointment.save()

    return redirect('index')
