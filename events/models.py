from django.db import models
from django.contrib.auth import get_user_model
from wards.models import Ward
from datetime import datetime
from locations.models import Location

# Create your models here.

User=get_user_model()

class Event(models.Model):

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    long = models.DecimalField(max_digits=19, decimal_places=16, default='0.00')
    lat = models.DecimalField(max_digits=19, decimal_places=16, default='0.00')
    created_at = models.DateTimeField(auto_now_add = True)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=datetime.now, null=True)
    time = models.DateTimeField(default=datetime.now, null=True)
    running_duration = models.IntegerField(default=0)
    description = models.TextField(max_length=255, null=True)
    image = models.CharField(max_length=300, null=True, blank=True)
