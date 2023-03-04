from django.urls import path
from .views import add_barber, delete_barber, modify_barber, index

app_name = 'barber'

urlpatterns = [
    path('', index, name = 'index'),
    path('add_barber/', add_barber, name = 'add_barber'),
    path('delete_barber/<int:id>/', delete_barber, name = 'delete_barber'),
    path('modify_barber/', modify_barber, name = 'modify_barber'),
]
