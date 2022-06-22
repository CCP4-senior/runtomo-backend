from django.db import models

class LocationType(models.Model):
    name = models.TextField(max_length=200)
