from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from drf_yasg.utils import swagger_auto_schema
from .models import Location
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from django.contrib.auth import get_user_model

class LocationDetailView(generics.GenericAPIView):
    serializer_class = serializers.LocationDetailSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Retrieve an location")
    def get(self, request, location_id):
        
        #get location by primary key, which is location_id
        location = get_object_or_404(Location, pk=location_id)

        serializer = self.serializer_class(instance=location)

        return Response(data=serializer.data, status=status.HTTP_200_OK)