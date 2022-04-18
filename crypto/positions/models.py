from unicodedata import name
from django.db import models
from numpy import imag

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)

class Positions(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField()
    price = models.CharField(max_length=200)
    rank = models.CharField(max_length=20)
    market_cap = models.CharField(max_length=200)
    volume = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


