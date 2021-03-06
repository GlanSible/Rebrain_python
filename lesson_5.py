# Rebrain_Python lesson 5

# 1)
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


# 2)
list_dict = []

for splittend_line in log_list:
    splittend_line = splittend_line.split(' ')
    temp_dict = {}

    temp_dict['time'] = ' '.join(splittend_line[:3])
    temp_dict['pc_name'] = splittend_line[3]
    temp_dict['service_name'] = splittend_line[4].removesuffix(':')
    temp_dict['message'] = ' '.join(splittend_line[5:])

    list_dict.append(temp_dict)
print(f"2: {list_dict}")


# 3)
print(f"3: {[ dict['time'] for dict in list_dict]}")


# 4)
for d in list_dict:
    date_list = d['time'].split(' ')
    d['date'] = ' '.join(date_list[:2])
    d['time'] = date_list[2]
print(f"4: {[ d['time'] for d in list_dict]}")


# 5)
print(f"5: {[d['message'] for d in list_dict if d['pc_name'] == 'PC0078']}")


# 6,7)
log_dict = dict(enumerate(list_dict, start = 100))
print(f"7: {log_dict[104]['message']}")
