from dataclasses import field
from .models import Profile, RunnerType
from django.contrib.auth import get_user_model
from rest_framework import serializers

User=get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['runner_type']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

class RunnerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunnerType
        fields = ['id', 'name']