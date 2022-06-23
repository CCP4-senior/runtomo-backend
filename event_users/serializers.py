from models import EventUser
from rest_framework import serializers

class EventUserDetailSerializer(serializers.ModelSerializer):


    class Meta:
        model=EventUser
        fields = ['event', 'user', 'attending']