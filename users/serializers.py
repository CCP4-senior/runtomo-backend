from dataclasses import field
from unittest import runner

from pkg_resources import require
from .models import Profile, RunnerType
from django.contrib.auth import get_user_model
from rest_framework import serializers

User=get_user_model()

class RunnerTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunnerType
        fields = ['id', 'name']
        
class ProfileSerializer(serializers.ModelSerializer):
    runner_type = RunnerTypeSerializer(many=True, required=False)
    class Meta:
        model = Profile
        fields = ['id','runner_type']
        read_only_fields = ['id']

    def create(self, validated_data):
        runner_type = validated_data.pop('runner_type',[])
        profile = Profile.objects.create(**validated_data)

        auth_user = self.context['request'].user
        runner_obj = RunnerType.objects.get_or_create(
            user = auth_user,
            **runner_type,
            )
        profile.runner_type.add(runner_obj)
            
        return profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserDetailSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']