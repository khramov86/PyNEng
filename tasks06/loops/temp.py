print('Fast' in 'FastEthernet')

vlan = [10, 20, 30, 40]

print(10 in vlan)
r1 = {
    'IOS': '15.4',
    'IP': '10.255.0.1',
    'hostname': 'london_r1',
    'location': '21 New Globe Walk',
    'model': '4451',
    'vendor': 'Cisco'}

#В словаре in проводит проверку по ключу

print('IOS' in r1)
print('4451' in r1)

print('IOS' in r1 and 10 in vlan)
print('4451' not in r1)
print(not '4451' in r1)

"""
Оператор and
В Python оператор and возвращает не булево значение, а значение одного из операндов.

Если оба операнда являются истиной, результатом выражения будет последнее значение:
Если один из операторов является ложью, результатом выражения будет первое ложное значение:


Оператор or, как и оператор and, возвращает значение одного из операндов.

При оценке операндов возвращается первый истинный операнд:

"""
# -*- coding: utf-8 -*-

# username = input('Введите имя пользователя: ')
# password = input('Введите пароль: ')
#
# if len(password) < 8:
#     print('Пароль слишком короткий')
# elif username in password:
#     print('Пароль содержит имя пользователя')
# else:
#     print('Пароль для пользователя {} установлен'.format(username))

"""
Тернарное выражение
s = [1, 2, 3, 4]
result = True if len(s) > 5 else False
"""
# for key,value in r1.items():
#     print(key + ' => ' + value)
commands = ['switchport mode access', 'spanning-tree portfast', 'spanning-tree bpduguard enable']
fast_int = ['0/1','0/3','0/4','0/7','0/9','0/10','0/11']
access_template = ['switchport mode access',
                    'switchport access vlan',
                    'spanning-tree portfast',
                    'spanning-tree bpduguard enable']

fast_int = {'access': { '0/12':10, '0/14':11, '0/16':17, '0/17':150 }}

for intf, vlan in fast_int['access'].items():
     print('interface FastEthernet' + intf)
     for command in access_template:
         if command.endswith('access vlan'):
             print(' {} {}'.format(command, vlan))
         else:
             print(' {}'.format(command))
