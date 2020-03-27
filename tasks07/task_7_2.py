"""
To dowload file
wget --no-check-certificate https://raw.githubusercontent.com/natenka/pyneng-examples-exercises/master/exercises/07_files/config_sw1.txt
author Vladimir Khramov

"""
filename = input("Введите имя файла ")

ignore = ['duplex', 'alias', 'Current configuration']

def config_commands(filename):
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('!'):
                continue
            else:
                print(line)


if filename:
    config_commands(filename)
else:
    config_commands('config_sw1.txt')
