london_co = {
    'r1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': '21 New Globe Walk',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
devname = input("Введите имя устройства: ")
print()
if devname in london_co.keys():
    print(london_co.get(devname))
    temp = london_co.get(devname).keys()
    parname = input("Введите имя параметра: {}".format(str(temp)) + "\t").lower()
    if parname in london_co.get(devname):
        print(london_co.get(devname)[parname])
    else:
        print("Нет такого параметра")
# print(london_co.keys())

# for key in london_co.keys():
#     print(key + " " + london_co[key])



#
# if devname in london_co.keys():
#     print(london_co.values(devname))
# else:
#     print("Устройства нет в списке")