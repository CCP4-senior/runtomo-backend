from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from .models import PointOfInterest
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from drf_yasg.utils import swagger_auto_schema

import pointsofinterest

# Create your views here.


class PointOfInterestListView(generics.GenericAPIView):
    serializer_class = serializers.PointOfInterestListViewSerializer
    queryset = PointOfInterest.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(operation_summary="Retrieve list of all selectable Points of Interest")
    def get(self, request):
        pointsofinterest = PointOfInterest.objects.all().order_by('-id')
        serializer = self.serializer_class(instance=pointsofinterest, many=True)

        return Response(data = serializer.data, status=status.HTTP_200_OK)

class PointOfInterestDetailView(generics.GenericAPIView):
    serializer_class = serializers.PointOfInterestDetailViewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(operation_summary="Retrieve a specific PointOfInterest")
    def get(self, request, pointsofinterest_id):

        onepoint = get_object_or_404(PointOfInterest, pk=pointsofinterest_id)

        serializer = self.serializer_class(instance=onepoint)

        return Response(data=serializer.data, status=status.HTTP_200_OK)