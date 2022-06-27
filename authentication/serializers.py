from unittest import runner
from .models import User
from rest_framework import serializers
from users.serializers import ProfileSerializer
from users.models import Profile

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25, allow_null=False, allow_blank=False)
    email = serializers.EmailField(max_length=100, allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model=User
        fields=['username', 'email', 'password']

    def validate(self, attrs):
        username_exists = User.objects.filter(username = attrs['username']).exists()

        if username_exists:
            raise serializers.ValidationError(detail="Username already exists")

        email_exists = User.objects.filter(email = attrs['email']).exists()

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
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25, allow_null=True, allow_blank=True)
    email = serializers.EmailField(max_length=100, allow_null=False, allow_blank=False)

    class Meta:
        model=User
        fields=['username', 'email']

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "E-mail Address is already in use"})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "Username already exists"})
        return value
    
    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})
            
        instance.email = validated_data['email']
        instance.username = validated_data['username']

        instance.save()

        return instance