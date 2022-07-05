from multiprocessing import Event
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from event_comments.models import EventComments
from . import serializers
from events.models import Event

# Create your views here.

class EventCommentCreate(generics.CreateAPIView):
    serializer_class = serializers.EventCommentsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return EventComments.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        event = Event.objects.get(pk=pk)

        event_user = self.request.user
        event_comments_queryset =EventComments.objects.filter(
            event=event, event_user=event_user)

        event.save()

        serializer.save(event=event, event_user=event_user)