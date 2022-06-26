from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, viewsets, mixins
from rest_framework.response import Response
from . import serializers
from drf_yasg.utils import swagger_auto_schema
from .models import Profile, RunnerLevel
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator

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

    @swagger_auto_schema(operation_summary="Retrieve a user by id")
    def get(self, request, user_id):

        users = get_object_or_404(User, pk=user_id)
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

        #get profile by primary key, which is profile
        profile = get_object_or_404(Profile, pk=user_id)

        serializer = self.serializer_class(data=data, instance=profile)

        if serializer.is_valid():
            serializer.save()

            return Response(data=serializer.data, status=status.HTTP_200_OK)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(name='create', decorator=swagger_auto_schema(
    operation_summary="Create a Profile (For a logged in User)"
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_summary="Update a Profile by Profile ID"
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_summary="Partial Update a Profile by Profile ID"
))

class ProfileViewSet(mixins.UpdateModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = serializers.ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        data = self.request.data
        serializer = self.serializer_class(data=data, context={"request":self.request})

        user = self.request.user
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(name='list', decorator=swagger_auto_schema(
    operation_summary="List all Runner Level"
))
@method_decorator(name='update', decorator=swagger_auto_schema(
    operation_summary="Update a Runner Level (Whole Object)"
))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(
    operation_summary="Partial Update a Runner Level"
))
@method_decorator(name='destroy', decorator=swagger_auto_schema(
    operation_summary="Remove a Runner Level"
))
class RunnerLevelViewSet(mixins.DestroyModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = serializers.RunnerLevelSerializer
    queryset = RunnerLevel.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')
