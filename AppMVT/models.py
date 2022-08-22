from django.db import models

class familiar(models.Model):
    nombre=models.CharField(max_length=20)
    edad=models.IntegerField()
    parentesco=models.CharField(max_length=20)
    nacimiento=models.DateField()