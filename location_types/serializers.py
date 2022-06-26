from .models import LocationType
from rest_framework import serializers

class LocationTypeCreationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)

    class Meta:
        model=LocationType
        fields = ['id', 'name']

class LocationTypeDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200)

    class Meta:
        model=LocationType
        fields = ['id', 'name']