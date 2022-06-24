from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from drf_yasg.utils import swagger_auto_schema
from .models import LocationType
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from django.contrib.auth import get_user_model

class LocationTypeDetailView(generics.GenericAPIView):
    serializer_class = serializers.LocationTypeDetailSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Retrieve a location")
    def get(self, request, location_type_id):
        
        #get location by primary key
        locationType = get_object_or_404(LocationType, pk=location_type_id)

        serializer = self.serializer_class(instance=locationType)

        return Response(data=serializer.data, status=status.HTTP_200_OK)