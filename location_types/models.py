from django.db import models

class LocationType(models.Model):
    name = models.CharField(max_length=200)

    # def __str__(self):

    #     return f"{self.name}"
