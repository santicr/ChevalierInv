from django.urls import path
from .views import add_barber

urlpatterns = [
    path('add_barber/', add_barber, name = 'add_barber'),
]
