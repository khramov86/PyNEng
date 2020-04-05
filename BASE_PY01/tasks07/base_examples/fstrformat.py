ip = '10.1.1.1'
mask = 4

print(f'IP: {ip} mask {mask}')
# Same with .format
# print("IP: {ip}, mask: {mask}".format(ip=ip, mask=mask))

'''Очень важное отличие f-строк от format: f-строки это выражение, которое выполняется, а не просто строка. То есть, 
в случае с ipython, как только мы написали выражение и нажали Enter, оно выполнилось и вместо выражений {ip} и {mask} 
подставились значения переменных. 

Поэтому, например, нельзя сначала написать шаблон, а затем определить переменные,
'''

# Можно писать выражения
octets = ['10', '1', '1', '1']
mask = 24
# Кроме подстановки значений переменных, в фигурных скобках можно писать выражения:

print(f"IP: {'.'.join(octets)}, mask: {mask}")

print(type('.'.join(octets)))

# После двоеточия в f-строках можно указывать те же значения, что и при использовании format:

oct1, oct2, oct3, oct4 = [10, 1, 1, 1]
print(f'''
IP address:
{oct1:<8} {oct2:<8} {oct3:<8} {oct4:<8}
{oct1:08b} {oct1:08b} {oct1:08b} {oct1:08b}
      ''')

ip_list = ['10.1.1.1/24', '10.2.2.2/24', '10.3.3.3/24']

for ip_address in ip_list:
    ip, mask = ip_address.split('/')
    print(f"IP: {ip}, mask: {mask}")

intf_type = 'Gi'
intf_name = '0/3'

print(f'\ninterface {intf_type}/{intf_name}')

# Выравнивание столбцами

topology = [['sw1', 'Gi0/1', 'r1', 'Gi0/2'],
            ['sw1', 'Gi0/2', 'r2', 'Gi0/1'],
            ['sw1', 'Gi0/3', 'r3', 'Gi0/0'],
            ['sw1', 'Gi0/5', 'sw4', 'Gi0/2']]

width = 8

for connection in topology:
    l_device, l_port, r_device, r_port = connection
    print(f'{l_device:{width}} {l_port:{width}} {r_device:{width}} {r_port:{width}}')
    # print(l_device[:width], r_device[:width])

session_stats = {'done': 10, 'todo': 0}

if session_stats['todo']:
    print(f"Pomodoros done: {session_stats['done']}, TODO: {session_stats['todo']}")
else:
    print(f"Good job! All {session_stats['done']} pomodoros done!")

print(f'Количество подключений в топологии: {len(topology)}')
# 0 после двоеточия - заменяет нулями все пробелы для строки меньше 8 символов, b - переводит в двоичную систему
print(f'{int(oct1):08b} {int(oct2):08b} {int(oct3):08b} {int(oct4):08b}')