from wards.models import Ward
from .models import Event
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class creatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class EventCreationSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=255)
    location = serializers.CharField(max_length=255)
    ward = serializers.SlugRelatedField(queryset = Ward.objects.all(),slug_field = 'ward_name')

    class Meta:
        model=Event
        fields = ['id', 'creator', 'title', 'location', 'created_at', 'ward', 'date', 'time', 'running_duration', 'description', 'image', 'lat', 'long']
        depth = 1

class EventDetailSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=255)
    creator = creatorSerializer(read_only=True)
    location = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField('date created')
    ward = serializers.CharField(source='ward.ward_name', default=None)

    class Meta:
        model=Event
        fields = ['id', 'creator', 'title', 'location', 'ward', 'created_at', 'date', 'time', 'running_duration', 'description', 'image', 'lat', 'long'] 
        depth = 1
