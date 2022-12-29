from django.db import models

# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length = 60)
    quantity = models.IntegerField()