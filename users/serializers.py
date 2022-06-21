from dataclasses import field
from .models import Profile
from django.contrib.auth import get_user_model
from rest_framework import serializers

User=get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['runner_type']

# class UserSerializer(serializers.ModelSerializer):
#     profile = ProfileSerializer(required=True)
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']