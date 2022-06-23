from django.db import models
from events.models import Event
from django.contrib.auth import get_user_model

User=get_user_model()

class EventUser(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, on_delete=models.CASCADE)
    attending = models.BooleanField(default=False)