from django.shortcuts import render, redirect
from .forms import ReserveForm
from appointment.models import Appointment
from datetime import datetime, timedelta, time
from barber.models import Barber
from django.http import HttpResponseNotFound
from django.core.mail import EmailMessage
import uuid, calendar, locale
from django.contrib import messages as m

locale.setlocale(locale.LC_ALL, 'es_es')

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
            today = datetime.now()
            date_flag = False
            if date.day == today.day:
                print(date.day, today.day, today.hour - 5, new_time.hour)
                if today.hour - 5 == new_time.hour:
                    if today.minute + 30 <= new_time.hour:
                        date_flag = True
                elif today.hour - 5 < new_time.hour:
                    date_flag = True
            elif date.day > today.day:
                date_flag = True
            
            if date_flag:
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
            host = 'http://127.0.0.1:8000'
            link = redirect('cancel_reserve', str(new_appointment.cancel_uuid))
            new_appointment.save()
            body = f"""
            Este email es para confirmarte que tu reserva se ha hecho con éxito.
            Nombre del barbero: {barber.name} {barber.lastname1}
            Año: {date.year}, Mes: {calendar.month_name[date.month]}, Día: {date.day}
            Hora: {hour} en formato de 24 horas.
            Por favor estar 5 minutos antes de la cita para confirmarla!

            Gracias por elegirnos.
            Chevalier

            Para cancelar la cita, solo haga clic en el siguiente enlace:
            {host + link.url}
            """
            message = EmailMessage(
                subject = 'Reserva en Chevalier',
                body = body,
                from_email = 'santi-caicedo-rojas21@hotmail.com',
                to = [email]
            )
            message.send(fail_silently = False)

    return redirect('index')

def cancel_reserve(req, cancel_uuid: str):
    try:
        cancel_uuid = uuid.UUID(cancel_uuid).hex
    except:
        m.error(req, 'Página no encontrada')
        return HttpResponseNotFound(render(req, 'main/error.html'))
    appointment = Appointment.objects.filter(cancel_uuid = cancel_uuid)
    if len(appointment):
        appointment.delete()
        return render(req, 'appointment/cancel.html')
    m.error(req, 'Página no encontrada')
    return HttpResponseNotFound(render(req, 'main/error.html'))