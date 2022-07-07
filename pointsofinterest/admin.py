from django.contrib import admin
from .models import PointOfInterest
# Register your models here.

@admin.register(PointOfInterest)
class PointsOfInterestAdmin(admin.ModelAdmin):
    list_display=['id', 'en_title', 'jp_title', 'lat', 'long', 'address']