from django.contrib import admin
from .models import Profile, RunnerTag, RunnerLevel
# Register your models here.

admin.site.register(Profile)
admin.site.register(RunnerLevel)
admin.site.register(RunnerTag)