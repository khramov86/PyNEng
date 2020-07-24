import re

int_line = '  MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec,'
match = re.search('BW \d+', int_line)
print(match.group())

log2 = 'Oct  3 12:49:15.941: %SW_MATM-4-MACFLAP_NOTIF: Host f04d.a206.7fd6 in vlan 1 is flapping between port Gi0/5 and port Gi0/16'
print(re.search('Host (\S+) in vlan (\d+) is flapping between port (\S+) and port (\S+)', log2).groups())

# Выражение \d+ уже использовалось ранее - оно описывает одну или более цифр.
# Выражение \S+ описывает все символы, кроме whitespace (пробел, таб и другие).
"""
\d - любая цифра
\D - любое нечисловое значение
\s - пробельные символы
\S - все, кроме пробельные символы
\w - любая буква, цифра или нижнее подчеркивание
\W - все, кроме букв, цифр или нижнего подчеркивания
"""
log = '*Jul  7 06:15:18.695: %LINEPROTO-5-UPDOWN: Line protocol on Interface Ethernet0/3, changed state to down'
print(re.search('\d\d:\d\d:\d\d', log).group())

print("{}".format(re.search('\w\w\w\w\.\w\w\w\w\.\w\w\w\w', log2).group()))

"""
regex+ - одно или более повторений предшествующего элемента
regex* - ноль или более повторений предшествующего элемента
regex? - ноль или одно повторение предшествующего элемента
regex{n} - ровно n повторений предшествующего элемента
regex{n,m} - от n до m повторений предшествующего элемента
regex{n, } - n или более повторений предшествующего элемента
"""

line = '100     aab1.a1a1.a5d3    FastEthernet0/1'
print(re.search('(a1)+', line).group())
sh_ip_int_br = 'Ethernet0/1    192.168.200.1   YES NVRAM  up          up'
print(re.search('\d+\.\d+\.\d+\.\d+', sh_ip_int_br).group())

print(re.search('\d+\s+\S+', line).group())
# Выражение ba* означает b, а затем ноль или более повторений a:
print(re.search('ba*', line).group())
email1 = 'user1@gmail.com'

print(re.search('\w+@\w+\.\w+', email1).group())
while True:
    mail = input("Введите email")
    if re.search('\w+\.*\w+@\w+\.\w+', mail) is not None:
        print(mail)
        break

# Но такое выражение не подходит для электронного адреса с точкой:
"""
. - любой символ, кроме символа новой строки
^ - начало строки
$ - конец строки
[abc] - любой символ в скобках
[^abc] - любой символ, кроме тех, что в скобках
a|b - элемент a или b
(regex) - выражение рассматривается как один элемент. Кроме того, подстрока, которая совпала с выражением, запоминается
"""