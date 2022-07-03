from django.contrib import admin
from .models import Event

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'created_at', 'ward', 'date', 'time', 'running_duration', 'description', 'lat', 'long', 'participants']
    list_filter = ['location', 'created_at']