from dataclasses import field
from unittest import runner

from pkg_resources import require
from .models import Profile, RunnerLevel
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

User=get_user_model()

class RunnerLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunnerLevel
        fields = ['id', 'name']
        read_only_fields = ['id']

class ProfileSerializer(serializers.ModelSerializer):
    runner_type = serializers.ListField(child=serializers.CharField())
    runner_level = RunnerLevelSerializer(many=True, required=False)

    class Meta:
        model = Profile
        fields = ['id', 'age', 'runner_type','runner_level'] 
        read_only_fields = ['id']

    def create(self, validated_data):
        runner_level = validated_data.pop('runner_level', [])
        profile = Profile(**validated_data)

        profile.save()

        request = self.context.get('request', None)
        for item in runner_level:
            item_obj, created = RunnerLevel.objects.get_or_create(
                user=request.user,
                **item
            )
            profile.runner_level.add(item_obj)
        
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