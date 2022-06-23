from django.db import models
from django.conf import settings
from events.models import Event
from django.contrib.auth import get_user_model

User=get_user_model()

class EventUser(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='user')
    attending = models.BooleanField(default=False)