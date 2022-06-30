from dataclasses import field
import profile
from unittest import runner

from pkg_resources import require
from .models import Profile, RunnerLevel, RunnerTag
from django.contrib.auth import get_user_model
from rest_framework import serializers

User=get_user_model()

class RunnerLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunnerLevel
        fields = ['id', 'name']
        read_only_fields = ['id']

class RunnerTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunnerTag
        fields = ['id', 'name']
        read_only_fields = ['id']

class ProfileSerializer(serializers.ModelSerializer):
    runner_tag = RunnerTagSerializer(many=True, required=False)
    runner_level = RunnerLevelSerializer(many=True, required=False)
    age_calculated = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'age_calculated', 'image', 'runner_tag','runner_level', 'date_of_birth', 'run_frequency', 'estimated10k', 'estimated5k'] 
        read_only_fields = ['id']

    # Calcualte Age from date of birth (SerializerMethodField)
    def get_age_calculated(self, obj):
        import datetime
        today = datetime.date.today()
        if hasattr(obj, 'date_of_birth'):
            age_calculated = today.year - obj.date_of_birth.year - ((today.month, today.day) < (obj.date_of_birth.month, obj.date_of_birth.day))
            return age_calculated  
        else:
            request = self.context.get('request', None)
            # dob = request.profile.date_of_birth
            # print(dob)
            # age_calculated = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            return
            

    def _get_or_create_runner_level(self, runner_level, profile):
        request = self.context.get('request', None)
        # loop runner_level
        for item in runner_level:
            item_obj, created = RunnerLevel.objects.get_or_create(
                user=request.user,
                **item
            )
            profile.runner_level.add(item_obj)

    def _get_or_create_runner_tag(self, runner_tag, profile):
        request = self.context.get('request', None)

        # loop runner_tag
        for item in runner_tag:
            item_obj, created = RunnerTag.objects.get_or_create(
                user=request.user,
                **item
            )
            profile.runner_tag.add(item_obj)

    def create(self, validated_data):
        runner_level = validated_data.pop('runner_level', [])
        runner_tag = validated_data.pop('runner_tag', [])
        profile = Profile(**validated_data)

        user_id = self.context['request'].user.id

        # Validation: Send Error message when profile is exist
        if Profile.objects.filter(user_id=user_id).exists():
            raise serializers.ValidationError({"message": "Profile is already exist"})

        profile.save()
        self._get_or_create_runner_level(runner_level, profile)
        self._get_or_create_runner_tag(runner_tag, profile)
        
        
        return profile
    
    def update(self, instance, validated_data):
        runner_level = validated_data.pop('runner_level', None)
        runner_tag = validated_data.pop('runner_tag', None)

        if runner_level is not None:
            instance.runner_level.clear()
            self._get_or_create_runner_level(runner_level, instance)
        
        if runner_tag is not None:
            instance.runner_tag.clear()
            self._get_or_create_runner_tag(runner_tag, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserDetailSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile']