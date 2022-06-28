from wards.models import Ward
from .models import Event
from rest_framework import serializers

class EventCreationSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=255)
    location = serializers.CharField(max_length=255)
    ward = serializers.StringRelatedField()

    class Meta:
        model=Event
        fields = ['id', 'creator', 'title', 'location', 'created_at', 'ward', 'date', 'time', 'running_duration', 'description', 'image', 'lat', 'long']

class EventDetailSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=255)
    location = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField('date created')
    ward = serializers.StringRelatedField()

    class Meta:
        model=Event
        fields = ['id', 'creator', 'title', 'location', 'ward', 'created_at', 'date', 'time', 'running_duration', 'description', 'image', 'lat', 'long'] 
