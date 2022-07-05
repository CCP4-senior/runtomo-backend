from users.serializers import UserSerializer
from wards.models import Ward
from .models import Event
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class creatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ParticipantsSerializer(serializers.ModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'participants']
        depth = 1

class EventCreationSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=255)
    location = serializers.CharField(max_length=255)
    ward = serializers.SlugRelatedField(queryset = Ward.objects.all(),slug_field = 'ward_name')
    participants = ParticipantsSerializer(many=True)

    class Meta:
        model=Event
        fields = ['id', 'creator', 'title', 'location', 'created_at', 'ward', 'date', 'time', 'running_duration', 'description', 'image', 'lat', 'long', 'participants']
        depth = 1

class EventDetailSerializer(serializers.ModelSerializer):

    title = serializers.CharField(max_length=255)
    creator = creatorSerializer(read_only=True)
    location = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField('date created', read_only=True)
    ward = serializers.CharField(source='ward.ward_name', default=None, read_only=True)

    class Meta:
        model=Event
        fields = ['id', 'creator', 'title', 'location', 'ward', 'created_at', 'date', 'time', 'running_duration', 'description', 'image', 'lat', 'long', 'participants'] 
        depth = 1

