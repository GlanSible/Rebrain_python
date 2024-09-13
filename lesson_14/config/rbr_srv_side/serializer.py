from rest_framework import serializers
from .models import Server


class ServerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Server
        fields = ['id', 'ip_address', 'description', 'name']
