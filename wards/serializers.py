from .models import Ward
from rest_framework import serializers

class WardListView(serializers.ModelSerializer):

    ward_name = serializers.CharField(max_length=50)

    class Meta:
        model = Ward
        fields = ['id', 'ward_name']

class WardDetailView(serializers.ModelSerializer):

    ward_name = serializers.CharField(max_length=50)
    
    class Meta:
        model = Ward
        fields = ['id', 'ward_name']
