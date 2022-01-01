# Rebrain_Python lesson 8

# 1)
list_hdd = [
    {'id': 382, 'total': 999641890816, 'used': 228013805568},
    {'id': 385, 'total': 61686008768, 'used': 52522710872},
    {'id': 398, 'total': 149023482194, 'used': 83612310700},
    {'id': 400, 'total': 498830397039, 'used': 459995976927},
    {'id': 401, 'total': 93386008768, 'used': 65371350065},
    {'id': 402, 'total': 988242468378, 'used': 892424683789},
    {'id': 430, 'total': 49705846287, 'used': 9522710872},
]


# 2)
def func2(list_hdd):  
    for d in list_hdd:
        id_status = {}
        id_status['id'] = d['id']

        hdd_total_size = int(d['total'] / 1024 ** 3)
        hdd_used_space = int(d['used'] / 1024 ** 3)
        gb_free_space = hdd_total_size - hdd_used_space
        perc_free_space = 100 - int(hdd_used_space / hdd_total_size * 100)

        if gb_free_space < 10 or perc_free_space < 5:
            id_status.update(memory_status = 'memory_critical')
        elif gb_free_space < 30 or perc_free_space < 10:
            id_status.update(memory_status = 'memory_not_enough')
        else:
            id_status.update(memory_status = 'memory_ok')
        yield id_status  


# 3,4)
list_3 = [ dict(k, **v) for k, v in zip(list_hdd, func2(list_hdd)) ]
print(f"4: {list_3}")


# 5)
log = '''May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated
May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.
May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...
May 20 11:01:12 PC-00102 PackageKit: daemon start
May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...
May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00
May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"
May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device
May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio
May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.
May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.'''
log_list = log.split('\n')


# 6)
print(f"6: {sorted(log_list, key=lambda t: t[7:15])}")


# 7)
print(f"7: {list(filter(lambda a: a[16:24] == 'PC-00102', log_list))}")


# 8)
splitted_list = list(map( lambda a: a.split(" "), log_list))

list8 = [' '.join(sl[5:]) for sl in splitted_list if 'kernel' in sl[4]]
print(f"8: {list8}")
