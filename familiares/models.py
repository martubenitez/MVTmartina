from django.db import models

# Create your models here.
class familiar(models.Model):
    Tipo = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    nacimiento = models.DateField()