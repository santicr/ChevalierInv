from django.contrib import admin
from django.urls import path
from appointment.views import reserve, confirm_reserve
from django.views.generic import TemplateView

urlpatterns = [
    path('<int:barber_id>/', reserve, name = 'reserve'),
    path('confirm/<int:barber_id>/<str:date>', confirm_reserve, name = 'confirm_reserve')
]
