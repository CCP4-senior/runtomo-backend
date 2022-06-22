from django.contrib import admin
from .models import Profile, RunnerType
# Register your models here.

admin.site.register(Profile)
admin.site.register(RunnerType)

# from django.contrib import admin
# from .models import Event

# # Register your models here.

# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     list_display = ['title', 'location', 'created_at']
#     list_filter = ['location', 'created_at']