from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Server, ExtendedServerInfo

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'name', 'description', 'server_is_active')

@admin.register(ExtendedServerInfo)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('host_information', 'network', 'disk', 'memory', 'cpu', 'load_average')