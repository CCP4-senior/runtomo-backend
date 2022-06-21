from .models import Location
from rest_framework import serializers

class LocationCreationSerializer(serializers.modelSerializer):
    type = serializers.IntegerField()
    long = serializers.FloatField(read_only=True)
    lat = serializers.FloatField(read_only=True)

    class Meta:
        model=Location
        fields = ['id', 'type', 'long', 'lat']