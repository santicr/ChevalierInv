from django.db import models

# Create your models here.
class Barber(models.Model):
    name = models.CharField(max_length = 100)
    lastname1 = models.CharField(max_length = 100)
    lastname2 = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return f'{self.name} {self.lastname1} {self.lastname2} {self.id}'