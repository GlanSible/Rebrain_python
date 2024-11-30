from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializer import ServerSerializer, ServerSerializerShort, ExtendedServerInfoSerializer
from .models import Server, ExtendedServerInfo

class ServerViewSetShort(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializerShort

class ServerViewSet(generics.ListAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ExtendedServerInfoView(generics.ListAPIView):
    queryset = ExtendedServerInfo.objects.all()
    serializer_class = ExtendedServerInfoSerializer

class ServerAddView(generics.CreateAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ExtendedServerAddView(generics.CreateAPIView):

    queryset = ExtendedServerInfo.objects.all()
    serializer_class = ExtendedServerInfoSerializer

class ServerDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Server.objects.all()
    serializer_class = ServerSerializer

class ExtendedServerDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = ExtendedServerInfo.objects.all()
    serializer_class = ExtendedServerInfoSerializer
