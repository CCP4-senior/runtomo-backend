from django.db import models

class Location(models.Model):
    type = models.IntegerField()
    long = models.DecimalField(read_only=True)
    lat = models.DecimalField(read_only=True)
