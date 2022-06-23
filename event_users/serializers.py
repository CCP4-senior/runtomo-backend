from .models import EventUser
from rest_framework import serializers

class EventUserDetailSerializer(serializers.ModelSerializer):
    attending = serializers.BooleanField(default=False)

    class Meta:
        model=EventUser
        fields = ['id', 'attending']