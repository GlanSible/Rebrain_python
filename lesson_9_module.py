# Rebrain_Python lesson 9 module file

from os import getlogin
from psutil import virtual_memory

def get_pc_data():
    data = {}
    mem = virtual_memory()

    data["user_name"] = getlogin()
    data['memory_total'] = int(mem.total / 1024 ** 2)
    data['memory_used'] = int(mem.used / 1024 ** 2)
    data['memory_percent'] = int(mem.percent)
    return data
