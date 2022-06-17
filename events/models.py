from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User=get_user_model()

class Event(models.Model):


    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)


