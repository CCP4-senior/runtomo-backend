from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from .models import Ward
from rest_framework.response import Response
from . import serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class WardListView(generics.GenericAPIView):
    serializer_class = serializers.WardListView
    queryset = Ward.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(operation_summary="Retrieve list of all selectable wards")
    def get(self, request):
        wards = Ward.objects.all().order_by('-id')
        serializer = self.serializer_class(instance=wards, many=True)

        return Response(data = serializer.data, status=status.HTTP_200_OK)

class WardDetailView(generics.GenericAPIView):
    serializer_class = serializers.WardDetailView
    permission_classes = [IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(operation_summary="Retrieve a specific ward")
    def get(self, request, ward_id):

        ward = get_object_or_404(Ward, pk=ward_id)

        serializer = self.serializer_class(instance=ward)

        return Response(data=serializer.data, status=status.HTTP_200_OK)