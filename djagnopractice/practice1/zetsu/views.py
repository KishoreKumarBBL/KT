from django.core.serializers import serialize

from .serializer import Regserializer
from django.shortcuts import render
from rest_framework.response import responses, Response
from rest_framework import generics,status



# Create your views here.
class UserRegistration(generics.CreateAPIView):
    serializer_class = Regserializer

    def create(self, request):
        serializer = Regserializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data,status=status.HTTP_201_CREATED)

class UserLogin(generics.GenericAPIView):
     def post (self, request):
         user=request.data






