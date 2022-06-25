from .models import Event
from rest_framework import serializers

class EventCreationSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=255)
    location = serializers.CharField(max_length=255)

    class Meta:
        model=Event
        fields = ['id', 'title', 'location', 'created_at', 'ward', 'date', 'time', 'running_duration', 'description', 'image']

class EventDetailSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=255)
    location = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField('date created')

    class Meta:
        model=Event
        fields = ['id', 'title', 'location', 'ward', 'created_at', 'date', 'time', 'running_duration', 'description', 'image']

