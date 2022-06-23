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
    def get(self, request, event_user_id):
        
        #get location by primary key, which is location_id
        event_user = get_object_or_404(EventUser, pk=event_user_id)

        serializer = self.serializer_class(instance=event_user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)