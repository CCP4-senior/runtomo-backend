from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=1)
    runner_level = models.ManyToManyField('RunnerLevel')
    runner_tag = models.ManyToManyField('RunnerTag')
    image = models.CharField(max_length=300, null=True, blank=True)
    date_of_birth = models.DateField(max_length=8)
    run_frequency = models.CharField(max_length=255, null=True)
    estimated10k = models.CharField(max_length=255, null=True)
    estimated5k = models.CharField(max_length=255, null=True)

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