from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from drf_yasg.utils import swagger_auto_schema
from .models import EventUser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

class EventUserDetailView(generics.GenericAPIView):
    serializer_class = serializers.EventUserDetailSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Retrieve all users attending event")
    def get(self, request, event_id):
        
        event_users = EventUser.objects.all().filter(event=event_id)

        serializer = self.serializer_class(instance=event_users)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Update user attendance to event")
    def post(self, request, event_id):
        event = get_object_or_404(EventUser, event=event_id)
        data = request.data
        if data.attendance == False:
            data.attendance=True
        else: 
            data.attendance=False

        serializer = self.serializer_class(data=data, instance=event)
        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)