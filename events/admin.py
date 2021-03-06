from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'created_at', 'ward', 'date', 'time', 'running_duration', 'description', 'lat', 'long', 'list_participants']
    list_filter = ['location', 'created_at']

    def list_participants(self, obj):
        return "\n".join([p.username for p in obj.participants.all()])