import psutil
import requests
import socket
import json
import os
import platform

# Define host_info dict as data
host_full_info = {}

def host_information():
    host_information = {}
    host_information['name'] = platform.node()
    host_information['platform'] = platform.system()
    host_full_info['host_information'] = host_information
host_information()

def network_info():
    iface_dict = {}
    ip_dict = {}
    addr_templates = ['lo', 'docker', 'br-', 'veth']
    for snicaddr in psutil.net_if_addrs():
        if not snicaddr.startswith(tuple(addr_templates)):
            iface_dict['interface_name'] = snicaddr
            iface_dict['interface_status'] = 'up' if psutil.net_if_stats()[snicaddr][0] else 'down'
            ip_dict['public_address'] = str(requests.get('https://ifconfig.me/ip').text)
            ip_dict['local_address'] = psutil.net_if_addrs()[snicaddr][0][1]
        else:
            pass
        host_full_info['network'] = [iface_dict, ip_dict]
network_info()

def disk():
    disk_list = []
    for sdiskpart in psutil.disk_partitions():
        if not str(sdiskpart.device).startswith('/dev/loop'):
            disk_list.append(sdiskpart._asdict())
            host_full_info['disk'] = disk_list
disk()

def memory():
    #print(psutil.virtual_memory())
    host_full_info['memory'] = psutil.virtual_memory()._asdict()
memory()

def cpu():
    cpu ={}
    cpu['cpu_cores'] = psutil.cpu_count()
    cpu['cpu_physical_cores'] = psutil.cpu_count(logical=False)
    cpu['cpu_freqency'] = psutil.cpu_freq()
    host_full_info['cpu'] = cpu
cpu()

def load_average():
    load_average = dict(zip(['1 min', '5 min', '15 min'], psutil.getloadavg()))
    host_full_info['load_average'] = load_average
load_average()

print(host_full_info)


# r = requests.post('http://127.0.0.1:8000/api/servers/add', json=simple_psutil())

# print(f"Status Code: {r.status_code}, Response: {r.json()}")

'''
Программа должна обрабатывать данные о системе, полученные от утилиты psutil, и отправлять их на сервер с интервалом в 1 минуту в формате:
{'host_information': {'sysname': ..., 'hostname' : ...}, 
 'network': [{'interface': up/down, 'mtu': ... }...],
 'disk': [{'disk: ..., 'mountpoint': ..., 'file_system_type', 'total': ..., 'used': ....} ],
 'memory': {'memory_total': ..., 'memory_used': ..., 'memory_percent': ...}, 
 'cpu': {'cpu_cores': ..., 'cpu_physical_cores': ..., 'cpu_freqency': {...}}, 
 'load_average': {'1 min': ..., '5 min': ..., '15 min': ...}}}
'''