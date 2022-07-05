from django.db import models
from django.contrib.auth import get_user_model
from events.models import Event

# Create your models here.

User=get_user_model()

class EventComments(models.Model):
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=4096, null=True)
    created = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return str(self.comment_user) + " | " + str(self.text)

