from unittest import runner
from .models import User
from rest_framework import serializers
from users.serializers import ProfileSerializer
from users.models import Profile

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25, allow_null=False, allow_blank=False)
    email = serializers.EmailField(max_length=100, allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8, write_only=True)

    # When Creating Users, Profile should also be created
    profile = ProfileSerializer(required=True)
    class Meta:
        model=User
        fields=['username', 'email', 'password', 'profile']

        def validate(self, attrs):
            username_exists = User.objects.filter(username = attrs['username']).exists()

            if username_exists:
                raise serializers.ValidationError(detail="Username already exists")

            email_exists = User.objects.filter(username = attrs['email']).exists()

            if email_exists:
                raise serializers.ValidationError(detail="E-mail Address is already in use")

            return super().validate(attrs)
            

    def create(self, validated_data):
        # create user
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],     
        )

        user.set_password(validated_data['password'])

        user.save()

        # create profile
        profile_data = validated_data.pop('profile')
        profile = Profile.objects.create(
            user = user,
            runner_type = profile_data['runner_type'],
        )

        return user