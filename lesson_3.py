# Rebrain_Python lesson 3

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


# 2,3)
dict_2_3 = {}
el_num = int(input())
splittend_list_el = log_list[el_num].split(' ')

dict_2_3['time'] = ' '.join(splittend_list_el[:3])
dict_2_3['pc_name'] = splittend_list_el[3]
dict_2_3['service_name'] = splittend_list_el[4].removesuffix(':')
dict_2_3['message'] = ' '.join(splittend_list_el[5:])

print(dict_2_3['pc_name'])


# 4)
list_4 = ['May 26 12:48:18', 'ideapad', 'systemd[1]', 'Finished Message of the Day.']
dict_keys = ['time', 'pc_name', 'service_name', 'message']

dict_4 = dict(zip(dict_keys, list_4))


# 5)
list_5 = (dict_2_3, dict_4)

print(list_5)


# 6)
set_1 = set(list_5[0].values())
set_2 = set(list_5[1].values())

print(set_1 & set_2)
