from django.contrib import admin
from .models import Location

# Register your models here.

@admin.register(Location)
class EventAdmin(admin.ModelAdmin):
    list_display = ['type', 'long', 'lat']
    list_filter = ['type', 'long', 'lat']