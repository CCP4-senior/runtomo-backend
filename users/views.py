from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from . import serializers
from drf_yasg.utils import swagger_auto_schema
from .models import Profile, RunnerType
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from django.contrib.auth import get_user_model

User = get_user_model()

class UserListView(generics.GenericAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = serializers.UserSerializer

    @swagger_auto_schema(operation_summary="List all Users")
    def get(self, request):

        users = User.objects.all()

        serializer = self.serializer_class(instance=users, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class UserDetailView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.UserDetailSerializer

    @swagger_auto_schema(operation_summary="Retrieve a user by username")
    def get(self, request, id):

        users = get_object_or_404(User, pk=id)
        serializer = self.serializer_class(instance=users)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

class RunnerTypeListView(generics.GenericAPIView):
    serializer_class = serializers.RunnerTypeSerializer

    @swagger_auto_schema(operation_summary="List all Runner Types")
    def get(self, request):

        runner_types = RunnerType.objects.all()

        serializer = self.serializer_class(instance=runner_types, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class ProfileCreateListView(generics.GenericAPIView):
    serializer_class = serializers.ProfileSerializer

    @swagger_auto_schema(operation_summary="Create a new Profile")
    def post(self, request, id):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      