"""
Скрипт должен запрашивать у пользователя:

информацию о режиме интерфейса (access/trunk)
номере интерфейса (тип и номер, вида Gi0/3)
номер VLANа (для режима trunk будет вводиться список VLANов)
"""

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]


def iface_info(iface_mode):
    iface_num = input("Введите тип и номер интерфейса: ")
    if(iface_mode == 'trunk'):
        iface_vlan = input("Введите разрешенные VLANы: ")
    elif (iface_mode == 'access'):
        iface_vlan = input("Введите номер влан(ов): ")
    return iface_num, iface_vlan

def selectiface(iface_mode):
    if iface_mode == 'trunk':
        iface_num, iface_vlan = iface_info(iface_mode)
        print("interface {}".format(iface_num))
        for item in trunk_template:
            if item.find('vlan {}'):
                print(item.format(iface_vlan))
            else:
                print("{} : ".format(item))
    elif iface_mode == 'access':
        iface_num, iface_vlan = iface_info(iface_mode)
        print("interface {}".format(iface_mode))
        for item in access_template:
            if item.find('vlan {}'):
                print(item.format(iface_vlan))
            else:
                print("{} : ".format(item))

    else:
        print("Incompatable iface mode")


def main():
    iface_mode = input("Введите режим работы интерфейса (access/trunk): ")
    selectiface(iface_mode)

main()