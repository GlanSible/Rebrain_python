import psutil
import requests
import json
import platform
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def host_full_info():
    # Define host_full_info dict as data structure
    host_full_info = {}

    logging.info("Start to gather info about system:")

    logging.info("Gathering Host information:")
    host_information = {}
    host_information['name'] = platform.node()
    host_information['platform'] = platform.system()
    host_full_info['host_information'] = host_information

    logging.info("Gathering Network information:")
    iface_dict = {}
    ip_dict = {}
    addr_templates = ['lo', 'docker', 'br-', 'veth']
    for snicaddr in psutil.net_if_addrs():
        if not snicaddr.startswith(tuple(addr_templates)):
            iface_dict['interface_name'] = snicaddr
            iface_dict['interface_status'] = 'up' if psutil.net_if_stats()[snicaddr][0] else 'down'
            ip_dict['local_address'] = psutil.net_if_addrs()[snicaddr][0][1]
            ip_dict['public_address'] = str(requests.get('https://ifconfig.me/ip').text)
        else:
            pass
        host_full_info['network'] = [iface_dict, ip_dict]

    logging.info("Gathering Disk information:")
    disk_list = []
    for sdiskpart in psutil.disk_partitions():
        if not str(sdiskpart.device).startswith('/dev/loop'):
            disk_list.append(sdiskpart._asdict())
            host_full_info['disk'] = disk_list

    logging.info("Gathering RAM information:")
    host_full_info['memory'] = psutil.virtual_memory()._asdict()
    # Iterate over memory dict to transform bytes into MiB
    for k, v in host_full_info['memory'].items():
        if v <= 100:
            pass
        else:
            v = round(v / 1024 ** 2)
            host_full_info['memory'][k] = v

    logging.info("Gathering CPU information:")
    cpu = {}
    cpu['cpu_cores'] = psutil.cpu_count()
    cpu['cpu_physical_cores'] = psutil.cpu_count(logical=False)
    cpu['cpu_freqency'] = psutil.cpu_freq()
    host_full_info['cpu'] = cpu

    logging.info("Gathering LA information:")
    load_average = dict(zip(['1 min', '5 min', '15 min'], psutil.getloadavg()))
    host_full_info['load_average'] = load_average
    # Round float values up to 2 signs
    for k, v in host_full_info['load_average'].items():
        v = round(v, 2)
        host_full_info['load_average'][k] = v

    logging.info("Serializing gathered data.")
    jsoned_host_full_info = json.dumps(host_full_info, indent=True)

    logging.info(f"""Gathered info about {host_full_info['host_information']['name']} server:
                 {jsoned_host_full_info}""")

    loaded_host_full_info = json.loads(jsoned_host_full_info)

    return loaded_host_full_info


try:
    r = requests.post(
        'http://127.0.0.1:8000/api/servers/add-extended',
        json=host_full_info())

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
else:
    logging.info("Data has been sucessfully sent.")
