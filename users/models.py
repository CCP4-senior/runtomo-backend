from django.forms import CharField
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # runner_type = ArrayField(models.CharField(max_length=200), blank=True)
    age = models.IntegerField(default=1)
    runner_level = models.ManyToManyField('RunnerLevel')
    runner_tag = models.ManyToManyField('RunnerTag')
    image = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f'{self.user} Profile'

class RunnerTag(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class RunnerLevel(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name