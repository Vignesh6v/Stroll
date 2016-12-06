from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length = 100, blank=True)
    email = models.EmailField()
    password = models.CharField(max_length = 100)
    lastName = models.CharField(max_length = 100)
    firstName = models.CharField(max_length = 100)
