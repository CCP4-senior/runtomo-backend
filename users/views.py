from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
# from serializers import UserSerializer
from . import serializers
from drf_yasg.utils import swagger_auto_schema
from .models import Profile
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from django.contrib.auth import get_user_model

User = get_user_model()

class UserListView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UserSerializer

    @swagger_auto_schema(operation_summary="List all Users")
    def get(self, request):

        users = User.objects.all()

        serializer = self.serializer_class(instance=users, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

      