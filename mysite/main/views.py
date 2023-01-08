from django.shortcuts import render
from barber.models import Barber
from datetime import datetime

# Create your views here.
def convert(x):
    if x >= 1 and x <= 9:
        return f'0{x}'
    return str(x)

def index(req):
    barbers = Barber.objects.all()
    today = str(datetime.now().year) + '-' + convert(datetime.now().month) + '-' + convert(datetime.now().day)
    max_val = str(datetime.now().year + 1) + '-' + convert(datetime.now().month) + '-' + convert(datetime.now().day)
    return render(req, 'main/index.html', {'barbers': barbers, 'min': today, 'value': today, 'max': max_val})