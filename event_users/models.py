from django.db import models
from django.conf import settings
from events.models import Event
from django.contrib.auth import get_user_model

User=get_user_model()

class EventUser(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def add_user_attendance(self, user):
        registration = EventUser.objects.create(user = user, event = self)
        registration.save()

    def remove_user_attendance(self, user):
        registration = EventUser.objects.get(user = user, event = self)
        registration.delete()