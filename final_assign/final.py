import psutil
import requests
import json
import platform
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define host_full_info dict as data structure
host_full_info = {}

logging.info("Start to gather info about system:")


def host_information():
    logging.info("Gathering Host information:")
    host_information = {}
    host_information['name'] = platform.node()
    host_information['platform'] = platform.system()
    host_full_info['host_information'] = host_information


host_information()


def network_info():
    logging.info("Gathering Network information:")
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
    logging.info("Gathering Disk information:")
    disk_list = []
    for sdiskpart in psutil.disk_partitions():
        if not str(sdiskpart.device).startswith('/dev/loop'):
            disk_list.append(sdiskpart._asdict())
            host_full_info['disk'] = disk_list


disk()


def memory():
    logging.info("Gathering RAM information:")
    # need to switch values to Mb
    host_full_info['memory'] = psutil.virtual_memory()._asdict()


memory()


def cpu():
    logging.info("Gathering CPU information:")
    cpu = {}
    cpu['cpu_cores'] = psutil.cpu_count()
    cpu['cpu_physical_cores'] = psutil.cpu_count(logical=False)
    cpu['cpu_freqency'] = psutil.cpu_freq()
    host_full_info['cpu'] = cpu


cpu()


def load_average():
    logging.info("Gathering LA information:")
    load_average = dict(zip(['1 min', '5 min', '15 min'], psutil.getloadavg()))
    host_full_info['load_average'] = load_average


load_average()


jsoned_host_full_info = json.dumps(host_full_info, indent=True)
# logging.info(f"""Gathered info {host_full_info['host_information']['name']} server: {jsoned_host_full_info}""")

loaded_host_full_info = json.loads(jsoned_host_full_info)

try:
    r = requests.post('http://127.0.0.1:8000/api/servers/add',
                       json=loaded_host_full_info)
    r.raise_for_status()
except requests.Timeout as e:
    logging.error(f"Server timeout: {e}")
except requests.ConnectionError as e:
    logging.error(f"Connection error: {e}")
except requests.RequestException as e:
    if r.status_code == 400:
        logging.error(f"{e}")
    else:
        logging.error(f"Request exception: {e}")
