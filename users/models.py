from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    runner_type = models.ForeignKey('RunnerType', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

class RunnerType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
