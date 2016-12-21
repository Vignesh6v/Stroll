from __future__ import unicode_literals

from django.db import models

class Tour(models.Model):
    tourid = models.CharField(max_length = 100, blank=True)
    name = models.CharField(max_length = 25)
    createdBy = models.CharField(max_length = 25)
    category = models.CharField(max_length = 100)
    time = models.CharField(max_length = 25)
    distance = models.CharField(max_length = 25)
    stops = models.PositiveIntegerField()
    latitude = models.CharField(max_length = 25)
    longitude = models.CharField(max_length = 25)


class Stops(models.Model):
    stopid = models.CharField(max_length = 100, blank=True)
    sequence = models.PositiveIntegerField()
    name = models.CharField(max_length = 25)
    stop_latitude = models.CharField(max_length = 25)
    stop_longitude = models.CharField(max_length = 25)
    description = models.CharField(max_length = 100)


class Upload(models.Model):
    name = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="cloud-stroll-images/", null=True, blank=True)
