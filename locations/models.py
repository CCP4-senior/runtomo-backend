from django.db import models
from location_types.models import LocationType

class Location(models.Model):
    type = models.ForeignKey(LocationType, on_delete=models.CASCADE)
    long = models.DecimalField(read_only=True, max_digits=19, decimal_places=16)
    lat = models.DecimalField(read_only=True, max_digits=18, decimal_places=16)
