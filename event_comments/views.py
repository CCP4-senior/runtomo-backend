from multiprocessing import Event
from django.shortcuts import render
from rest_framework import generics, status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

from event_comments.models import EventComments
from . import permissions
from . import serializers
from events.models import Event

# Create your views here.

@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_summary="Create a comment for an event by event id"
))
class EventCommentCreate(generics.CreateAPIView):
    serializer_class = serializers.EventCommentsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return EventComments.objects.all()

    @swagger_auto_schema(operation_description="sth")
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        event = Event.objects.get(pk=pk)

        comment_user = self.request.user
        event_comments_queryset = EventComments.objects.filter(
            event=event, comment_user=comment_user)

        if serializer.is_valid():
            serializer.save(event=event, comment_user=comment_user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventCommentList(generics.ListAPIView):
    serializer_class = serializers.EventCommentsSerializer

    @swagger_auto_schema(operation_summary="Get comments by event id")
    def get_queryset(self):
        pk = self.kwargs['pk']
        return EventComments.objects.filter(event=pk)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventComments.objects.all()
    serializer_class = serializers.EventCommentsSerializer
    permission_classes = [permissions.IsCommentUserOrReadOnly]
