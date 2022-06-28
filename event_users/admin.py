from django.contrib import admin
from .models import EventUser

admin.site.register(EventUser)
class EventUser(admin.ModelAdmin):
    list_display = ['id', 'user', 'event']
    list_filter = ['id', 'user', 'event']