# Rebrain_Python lesson 10
import os
import sys
import time
import logging


logging.basicConfig(filename='log_file.log', format='%(asctime)s %(levelname)s %(message)s', datefmt='%b %d %H:%M:%S', level=logging.INFO)
argv_number = int(sys.argv[1])
argv_time = int(sys.argv[2])

os_key_list = list(os.environ.keys())[:argv_number]
os_val_list = list(os.environ.values())[:argv_number]
environ_dict = dict(zip(os_key_list, os_val_list))

for k,v in environ_dict.items():
  logging.info(f"{k} -> {v}")
  time.sleep(argv_time)
