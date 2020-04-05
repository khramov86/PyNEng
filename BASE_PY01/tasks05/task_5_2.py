"""
Пример требуемого вывода
Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

"""
import array as arr
def dectobin(decnum):
    a = arr.array('i', [])
    for i in range(0, len(str(decnum))):
        #a[i] =
        #print(a[i])
        pass




dectobin(101010101)

address = input("Введите адрес в формате 10.1.1.0/24")
if address == '':
    address = '10.1.1.0/24'
network = address.split('/')
print(network)
ipaddr = network[0]
netmask = network[1]

print(ipaddr, netmask)

ipaddr = ipaddr.split('.')
# for octet in ipaddr:
#     print("Number in dec " + octet + "  in binary: " + oct(int(octet)))
#
