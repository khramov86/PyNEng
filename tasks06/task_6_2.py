# ip = input("Введите ip-адрес: ")
#
# for octet in ip:
#     print(octet)

# if ip == '':
#     ip = '192.168.120.1'
#     print("IP по умолчанию: " + ip)
"""
„unicast“ - если первый байт в диапазоне 1-223
„multicast“ - если первый байт в диапазоне 224-239
„local broadcast“ - если IP-адрес равен 255.255.255.255
„unassigned“ - если IP-адрес равен 0.0.0.0
„unused“ - во всех остальных случаях
"""


def check_ip(ip):
    check_status = True
    octet = ip.split('.')
    if len(octet) == 4:
        for num in octet:
            print(num)
            for i in range(0, 256):
                if num != i:
                    check_status == False
                    break
    if check_status:
        return True
    else:
        return False


def network_type(ip):
    octet = ip.split('.')
    #    print(octet[0])
    if ip == '0.0.0.0':
        print(ip + " unassigned")
    elif octet[0] in str(range(1, 223)):
        print(ip + " unicast")
    elif octet[0] in str(range(224, 239)):
        print(ip + " multicast")
    elif ip == '255.255.255.255':
        print(ip + " local broadcast")
    else:
        print(ip + " unused")


def test():
    print("Проверка для unicast")
    network_type('1.0.0.0')
    network_type('223.0.0.0')
    print("Проверка для multicast")
    network_type('224.0.0.0')
    network_type('239.0.0.0')
    print("Проверка для local broadcast")
    network_type('255.255.255.255')
    print("Проверка для unassigned")
    network_type('0.0.0.0')
    print("Проверка на unused")
    network_type('test')
    network_type('0.1.1.1')

test()
print(check_ip("255.257.120.1"))
