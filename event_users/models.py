from django.db import models
from events.models import Event
from django.contrib.auth import get_user_model


User=get_user_model()

class EventUser(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.event.title