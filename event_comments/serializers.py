from rest_framework import serializers
from .models import EventComments
from django.contrib.auth import get_user_model
User=get_user_model()

class CommentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class EventCommentsSerializer(serializers.ModelSerializer):
    comment_user = CommentUserSerializer(read_only=True)
    class Meta:
        model = EventComments
        exclude = ('event',)
        # fields = "__all__"
        depth = 1
