from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .models import User
from . import serializers

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

# class UserUpdateView(generics.GenericAPIView):
#     serializer_class = serializers.UserUpdateSerializer    
#     @swagger_auto_schema(operation_summary="Update a user account")
#     def put(self, request, id):
#         user = self.get_object(id)
#         serializer = self.serializer_class(user, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_201_CREATED)

#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)