from django.contrib import admin
from .models import LocationType

# Register your models here.

@admin.register(LocationType)
class Admin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']