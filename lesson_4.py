# Rebrain_Python lesson 4

list_hdd = [
    {'total': 999641890816, 'used': 228013805568},
    {'total': 61686008768, 'used': 52522710872},
    {'total': 149023482194, 'used': 83612310700},
    {'total': 498830397039, 'used': 459995976927},
    {'total': 93386008768, 'used': 65371350065},
    {'total': 988242468378, 'used': 892424683789},
    {'total': 49705846287, 'used': 9522710872},
]

req_hdd = int(input("Choose hdd number (from 1 to 7): "))

real_hdd_number = req_hdd - 1
hdd_total_size = int(list_hdd[real_hdd_number]['total'] / 1024 ** 3)
hdd_used_space = int(list_hdd[real_hdd_number]['used'] / 1024 ** 3)
gb_free_space = hdd_total_size - hdd_used_space
perc_free_space = 100 - int(hdd_used_space / hdd_total_size * 100)
print(hdd_total_size, hdd_used_space, gb_free_space, perc_free_space)

if gb_free_space < 10 or perc_free_space < 5:
    print(f"на накопителе {req_hdd} критически мало свободного места")
elif gb_free_space < 30 or perc_free_space < 10:
    print(f"на накопителе {req_hdd} мало свободного места")
else:
    print(f"на накопителе {req_hdd} достаточно свободного места")
