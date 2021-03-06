from unittest import runner
from .models import User
from rest_framework import serializers
from users.serializers import ProfileSerializer
from users.models import Profile
from django.contrib.auth.password_validation import validate_password

class UserCreationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25, allow_null=False, allow_blank=False)
    email = serializers.EmailField(max_length=100, allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8, write_only=True)
    image = serializers.CharField(max_length=300, allow_null=True, allow_blank=True)

    class Meta:
        model=User
        fields=['username', 'email', 'password', 'image']

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
            image = validated_data['image']
        )

        user.set_password(validated_data['password'])

        user.save()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25, allow_null=True, allow_blank=True)
    email = serializers.EmailField(max_length=100, allow_null=True, allow_blank=True)
    image = serializers.CharField(max_length=300, allow_null=True, allow_blank=True)

    class Meta:
        model=User
        fields=['username', 'email', 'image']

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

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()

        return instance


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.save()

        return instance