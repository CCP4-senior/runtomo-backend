from django.db import models
from django.contrib.auth import get_user_model
from wards.models import Ward
from datetime import datetime

# Create your models here.

User=get_user_model()

class Event(models.Model):

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=datetime.now())
    time = models.DateTimeField(default=datetime.now())
    running_duration = models.IntegerField(default=0)
    description = models.TextField(max_length=255)
    image = models.CharField(max_length=300, null=True, blank=True)
