from dataclasses import field
from unittest import runner

from pkg_resources import require
from .models import Profile, RunnerLevel
from django.contrib.auth import get_user_model
from rest_framework import serializers

User=get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    # runner_type = RunnerTypeSerializer(many=False, required=False)
    runner_type = serializers.ListField(child=serializers.CharField())
    class Meta:
        model = Profile
        fields = ['runner_type', 'age']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserDetailSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']

class RunnerLevelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RunnerLevel
        fields = ['id', 'name']
        read_only_fields = ['id']