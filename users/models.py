from django.forms import CharField
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

gender = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('OTHER', 'Other'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    runner_type = ArrayField(models.CharField(max_length=200), blank=True)
    age = models.IntegerField(default=0)
    # gender = models.CharField(max_length=10, choices=gender)
    # runner_type = models.ForeignKey('RunnerType', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

class RunnerType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
