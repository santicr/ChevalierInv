from django.shortcuts import render
from .forms import ReserveForm

# Create your views here.
def reserve(req):
    form = ReserveForm()
    return render(req, 'appointment/reserve.html', {'form': form})