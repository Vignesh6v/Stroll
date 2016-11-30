from __future__ import unicode_literals

from django.db import models

class Tour(models.Model):
    id = models.CharField(primary_key=True,max_length=25)
    name = models.CharField(max_length = 25)
    createdBy = models.EmailField()
    category = models.CharField(max_length = 100)
    time = models.PositiveIntegerField()
    distance = models.PositiveIntegerField()
    stops = models.PositiveIntegerField()
    latitude = models.DecimalField(max_digits= 8, decimal_places = 6)
    longitude = models.DecimalField(max_digits = 8, decimal_places = 6)
