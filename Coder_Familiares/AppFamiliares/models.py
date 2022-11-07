from django.db import models

# Create your models here.

class ListadeFamiliares(models.Model):

    name = models.CharField(max_length=40)
    date = models.DateField()
    age = models.IntegerField()
    