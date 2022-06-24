from django.contrib import admin
from .models import Event

# Register your models here.

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'created_at', 'ward', 'date', 'time', 'running_duration', 'description']
    # list_display = ['title', 'location', 'created_at', 'ward', 'running_duration', 'description']
    list_filter = ['location', 'created_at']