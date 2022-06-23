from django.contrib import admin
from .models import Ward

# Register your models here.

@admin.register(Ward)
class WardsAdmin(admin.ModelAdmin):
    list_display=['id', 'ward_name']