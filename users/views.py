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

class ProfileCreateListView(generics.GenericAPIView):
    serializer_class = serializers.ProfileSerializer
    queryset = Profile.objects.all()
    
    @swagger_auto_schema(operation_summary="List all profiles")
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = self.serializer_class(instance=profiles, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Create a new Profile")
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        user = request.user
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Update a Profile by user id ")
    def put(self, request, user_id):
        data = request.data

        #get event by primary key, which is event_id
        profile = get_object_or_404(Profile, pk=user_id)

        serializer = self.serializer_class(data=data, instance=profile)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)