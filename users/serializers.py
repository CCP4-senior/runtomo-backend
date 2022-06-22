from dataclasses import field
from unittest import runner
from .models import Profile, RunnerType
from django.contrib.auth import get_user_model
from rest_framework import serializers

User=get_user_model()

class RunnerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunnerType
        fields = ['id', 'name']
        
class ProfileSerializer(serializers.ModelSerializer):
    runner_type = RunnerTypeSerializer(required=True)
    class Meta:
        model = Profile
        fields = ['runner_type']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserDetailSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']