from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializer import ServerSerializer, ServerSerializerShort
from .models import Server

class ServerViewSetShort(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializerShort

class ServerViewSet(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerAddView(generics.CreateAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ServerDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer
