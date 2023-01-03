from django.db import models
from barber.models import Barber

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length = 150)
    lastname1 = models.CharField(max_length = 150)
    lastname2 = models.CharField(max_length = 150)
    email = models.EmailField()
    date = models.DateField()
    hour = models.TimeField()
    barber = models.ForeignKey(Barber, on_delete = models.PROTECT)

    def __str__(self) -> str:
        return f'Cita {self.id} con el barbero {self.barber} y con hora {self.hour}'