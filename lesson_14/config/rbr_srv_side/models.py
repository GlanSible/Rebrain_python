# Create your models here.
from django.db import models

class Server(models.Model):

    name             = models.CharField('name', max_length=255)
    ip_address       = models.GenericIPAddressField('IP', max_length=16, default='0.0.0.0')
    description      = models.TextField('description', max_length=255, default='no_description')
    server_is_active = models.BooleanField('server status', default=False)

    class Meta:
        managed      = True
        verbose_name = 'Server'

class ExtendedServerInfo(models.Model):

    host_information = models.JSONField('host_information')
    network          = models.JSONField('network')
    disk             = models.JSONField('disk')
    memory           = models.JSONField('memory')
    cpu              = models.JSONField('cpu')
    load_average     = models.JSONField('load_average')

    class Meta:
        managed      = True
        verbose_name = 'extended-server-info'
