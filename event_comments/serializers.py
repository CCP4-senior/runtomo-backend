from rest_framework import serializers
from .models import EventComments

class EventCommentsSerializer(serializers.ModelSerializer):
    comment_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = EventComments
        exclude = ('event',)
        # fields = "__all__"