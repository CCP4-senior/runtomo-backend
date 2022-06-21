from django.db import models

class Location(models.Model):
    type = models.IntegerField()
    long = models.FloatField(read_only=True)
    lat = models.FloatField(read_only=True)
