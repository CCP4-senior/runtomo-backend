from django.shortcuts import render
from rest_framework import generics, status, viewsets, mixins
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import User
from . import serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from django.utils.decorators import method_decorator

# Create your views here.
class HelloAuthView(generics.GenericAPIView):
    @swagger_auto_schema(operation_summary="Hello authentication page!")
    def get(self,request):
        return Response(data={"message":"Hello Auth"},status=status.HTTP_200_OK)

class UserCreateView(generics.GenericAPIView):
    serializer_class = serializers.UserCreationSerializer    
    @swagger_auto_schema(operation_summary="Create a user account")
    def post(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.ChangePasswordSerializer

    def get_queryset(self):
       data = User.objects.all()
       return data

    def update(self, request, *args, **kwargs):
        data = self.request.data
        serializer = self.serializer_class(data=data, context={"request":self.request})

        if serializer.is_valid():
            return Response(data={"message":"Password has been changed successfully."}, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDeleteView(generics.GenericAPIView):
    serializer_class = serializers.UserCreationSerializer    
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="Delete a user account + Profile")
    def delete(self, request):
        user=self.request.user
        user.delete()

        return Response({"message": "User is deleted!"})
        