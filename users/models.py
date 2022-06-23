from django.forms import CharField
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth import get_user_model
from django.forms import CharField

User=get_user_model()

test_types = (
    ('AVID', 'Avid'),
    ('COMPETITIVE', 'Competitive'),
    ('FAST', 'Fast')
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    runner_type = ArrayField(models.CharField(max_length=200), blank=True)
    age = models.fields.IntegerField(max_value=None, min_value=None)

    def __str__(self):
        return f'{self.user.username} Profile'

class RunnerType(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
