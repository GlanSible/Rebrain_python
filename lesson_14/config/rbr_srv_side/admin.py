from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Server

@admin.register(Server)
class ServerAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'name', 'description')
