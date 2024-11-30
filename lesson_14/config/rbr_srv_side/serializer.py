from rest_framework import serializers
from .models import Server, ExtendedServerInfo


class ServerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = ['id', 'ip_address', 'description', 'name', 'server_is_active']

class ServerSerializerShort(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = ['ip_address', 'server_is_active']

class ExtendedServerInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExtendedServerInfo
        fields = ['host_information', 'network', 'disk', 'memory', 'cpu', 'load_average']
