# https://pyneng.readthedocs.io/ru/latest/exercises/06_exercises.html

access_template = [
    'switchport mode access', 'switchport access vlan',
    'spanning-tree portfast', 'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan'
]

access = {
    '0/12': '10',
    '0/14': '11',
    '0/16': '17',
    '0/17': '150'
}
trunk = {
    '0/1': ['add', '10', '20'],
    '0/2': ['only', '11', '30'],
    '0/4': ['del', '17'],
    '': ''
}
#
# for intf, vlan in access.items():
#     print('interface FastEthernet ' + intf)
#     for command in access_template:
#         if command.endswith('access vlan'):
#             print(' {} {}'.format(command, vlan))
#         else:
#             print(' {}'.format(command))

for tr, vlan in trunk.items():
    print('Trunk number is ' + tr)
    # print(tr, vlan)
    print('Execute this command:')
    for command in trunk_template:
        # print('Комманды для транка ' + command)
        if vlan == '':
            break
        if command.endswith('allowed vlan'):
            if vlan[0] == 'add':
                print('{} add {}'.format(command, ','.join(vlan[1:])))
            elif vlan[0] == 'del':
                print('{} remove {}'.format(command, ','.join(vlan[1:])))
            elif vlan[0] == 'only':
                print('{} {}'.format(command, ','.join(vlan[1:])))
            else:
                print('Something went wrong')
                break
    print()
