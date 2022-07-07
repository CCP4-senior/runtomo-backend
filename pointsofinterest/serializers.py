from .models import PointOfInterest
from rest_framework import serializers

class PointOfInterestListViewSerializer(serializers.ModelSerializer):

    en_title = serializers.CharField(max_length=255)
    jp_title = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)

    class Meta:
        model = PointOfInterest
        fields = ['id', 'en_title', 'jp_title', 'lat', 'long', 'address']

class PointOfInterestDetailViewSerializer(serializers.ModelSerializer):
    en_title = serializers.CharField(max_length=255)
    jp_title = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    
    class Meta:
        model = PointOfInterest
        fields = ['id', 'en_title', 'jp_title', 'lat', 'long', 'address']
