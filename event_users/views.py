from django.shortcuts import get_object_or_404
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

        serializer = self.serializer_class(instance=event_users, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Add user attendance")
    def post(self, request, event_id):

        event = get_object_or_404(Event, event=event_id)
        newAttendee = EventUser.objects.create(user=self, event=event)

        serializer = self.serializer_class(instance=newAttendee)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Remove user attendance")
    def delete(self, request, event_id):

        userAttendance = EventUser.objects.get(user=self, event=event_id)

        userAttendance.delete()

        return Response(status=status.HTTP_200_OK)