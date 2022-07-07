# from asyncio.windows_events import NULL
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from drf_yasg.utils import swagger_auto_schema
from .models import Event
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.
class HelloEventsView(generics.GenericAPIView):
    @swagger_auto_schema(operation_summary="Hello events page!")
    def get(self, request):
        return Response(data={"message":"Hello Events"},status=status.HTTP_200_OK)

class EventCreateListView(generics.GenericAPIView):
    
    serializer_class = serializers.EventCreationSerializer
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Create a new event")
    def post(self, request):
        data = request.data
        user = request.user

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save(creator=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventsDetailViewAll(generics.GenericAPIView):
    serializer_class=serializers.EventDetailSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Show all events")
    def get(self, request):
        events = Event.objects.all().order_by('-created_at')

        serializer = self.serializer_class(instance=events, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class EventDetailView(generics.GenericAPIView):
    serializer_class = serializers.EventDetailSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Retrieve an event")
    def get(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)

        serializer = self.serializer_class(instance=event)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Update an event by event_id")
    def put(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        data = request.data

        serializer = self.serializer_class(data=data, instance=event)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Delete an event by event_id")
    def delete(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)

        event.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class UserEventsView(generics.GenericAPIView):
    serializer_class = serializers.EventDetailSerializer
    permission_classes = [IsAuthenticated]
    
    @swagger_auto_schema(operation_summary="Get specific events by a specific user")
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)

        events = Event.objects.all().filter(creator=user)

        serializer = self.serializer_class(instance=events, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class UserEventDetails(generics.GenericAPIView):
    serializer_class = serializers.EventDetailSerializer
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(operation_summary="Get a specific event by a specific user")
    def get(self, request, user_id, event_id):
        user = User.objects.get(pk=user_id)

        event = Event.objects.all().filter(creator=user).get(pk=event_id)

        serializer = self.serializer_class(instance=event)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class ParticipantDetails(generics.GenericAPIView):
    serializer_class = serializers.EventCreationSerializer
    permission_classes = [IsAuthenticated]
    @swagger_auto_schema(operation_summary="Find all participants of an event")
    def get(self, request, event_id):

        queryset = Event.objects.get(pk=event_id)
        serializer = self.serializer_class(instance=queryset)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Assign user as a participant")
    def post(self, request, event_id, user_id):
        user = User.objects.get(pk=user_id)
        event = Event.objects.get(pk=event_id)
        data = event.participants.add(user)
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
                
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(operation_summary="Remove user from event participants")
    def delete(self, request, event_id, user_id):
        user = User.objects.get(pk=user_id)        
        event = get_object_or_404(Event, pk=event_id)
        participant = event.participants.remove(user)
        event.participants.remove(participant)

        return Response(status=status.HTTP_204_NO_CONTENT)