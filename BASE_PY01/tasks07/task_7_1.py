# Задание 4.6
# Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
#
# Protocol:               OSPF
# Prefix:                 10.0.24.0/24
# AD/Metric:              110/41
# Next-Hop:               10.0.13.3
# Last update:            3d18h
# Outbound Interface:     FastEthernet0/0

with open('ospf.txt', 'r') as f:
    for line in f:
        # strip дает отображение по строкам
        # split раделяет строку по пробелу и откидывает все лишнии пробелы
        line = line.split()
        if line[0] == 'O':
            print("Protocol:\t {}".format("OSPF"))
            print("Prefix:\t {}".format(line[1]))
            print("AD/Metric: :\t {}".format(''.join(line[2:3]).strip('[').strip(']')))
            print("Next-Hop:\t {}".format(line[4].strip(',')))
            print("Last update:\t {}".format(line[5].strip(',')))
            print("Outbound Interface:\t {}".format(line[6].strip(',')))
        else:
            print("Protocol not found")
