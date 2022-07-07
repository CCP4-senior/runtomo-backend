from django.db import models

# Create your models here.

class PointOfInterest(models.Model):

    en_title = models.CharField(max_length=255)
    jp_title = models.CharField(max_length=255, blank=True, null=True)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    long = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
