def configure_intf(intf_name='', ip='', mask=''):
    """
    This is fuction, that returns Network iface info
    """
    print('interface', intf_name)
    if ip == '':
        print('ip address', ip, mask)
    else:
        print('your subnet is ', mask)
'''
Функция может возвращать несколько значений. В этом случае, они пишутся через запятую после оператора return. При этом фактически функция возвращает кортеж
'''

configure_intf('eth0', ' ', 24)
print(configure_intf.__doc__)