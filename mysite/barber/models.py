from django.db import models

# Create your models here.
class Barber(models.Model):
    name = models.CharField(max_length = 100)
    lastname1 = models.CharField(max_length = 100)
    lastname2 = models.CharField(max_length = 100)