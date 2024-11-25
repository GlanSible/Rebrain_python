import psutil
import requests
import socket
import json

# Define host_info dict as data

host_full_info = {}

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

def load_average():
    load_average = dict(zip(['1 min', '5 min', '15 min'], psutil.getloadavg()))
    host_full_info['load_average'] = load_average
load_average()
'''
def simple_psutil():
    host_information = {}
    # Used Socket module due to WSL having issues with psutil.users() output
    host_information['name'] = str(socket.gethostname())
    host_information['ip_address'] = str(requests.get('https://ifconfig.me/ip').text)
    host_information['description'] = str('local IP address is ' + network_info())

    # convert data to json
    host_information = json.dumps(host_information)
    loaded_host_information = json.loads(host_information)
    return loaded_host_information
'''
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