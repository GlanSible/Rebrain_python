import psutil
import requests
import socket
import json


# Define host_info dict as data
host_info = {}

def local_ip():
    for snicaddr in psutil.net_if_addrs():
        if snicaddr != 'lo':
            local_ip = psutil.net_if_addrs()[snicaddr][0][1]
            # local_ip = str(psutil.net_if_addrs().str(snicaddr).address)
            #print(local_ip)
        else:
            pass
    return local_ip
        

def simple_psutil():
    host_information = {}
    # Used Socket module due to WSL having issues with psutil.users() output
    host_information['name'] = str(socket.gethostname())
    host_information['ip_address'] = str(requests.get('https://ifconfig.me/ip').text)
    host_information['description'] = str('local IP address is ' + local_ip())

    # convert data to json
    host_information = json.dumps(host_information)
    loaded_host_information = json.loads(host_information)
    return loaded_host_information

print(simple_psutil())

r = requests.post('http://127.0.0.1:8000/api/servers/add', json=simple_psutil())

print(f"Status Code: {r.status_code}, Response: {r.json()}")
