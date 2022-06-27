from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from drf_yasg.utils import swagger_auto_schema
from .models import EventUser
from rest_framework.permissions import IsAuthenticated
from events.models import Event

class EventUserDetailView(generics.GenericAPIView):
    serializer_class = serializers.EventUserDetailSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Retrieve all users attending event")
    def get(self, request, event_id):
        
        event_users = EventUser.objects.all().filter(event=event_id)

        serializer = self.serializer_class(instance=event_users)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Add user attendance")
    def event_add_user(self, request, pk):

        chosen_event = Event.objects.get(pk=pk)

        chosen_event.add_user_attendance(user=request.user)

        serializer = self.serializer_class(instance=chosen_event)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Remove user attendance")
    def event_remove_user(self, request, pk):

        chosen_event = Event.objects.get(pk=pk)

        chosen_event.remove_user_attendance(request.user)

        serializer = self.serializer_class(instance=chosen_event)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    