"""
To dowload file
wget --no-check-certificate https://raw.githubusercontent.com/natenka/pyneng-examples-exercises/master/exercises/07_files/config_sw1.txt
author Vladimir Khramov

"""
import os

# filename = input("Введите имя файла ")

ignore = ['duplex', 'alias', 'Current configuration']


def config_commands(filename):
    with open(filename, 'r') as f:
        temp = ''
        for line in f:
            line = line.strip()
            if not line.startswith('!'):
                temp += line + '\n'
        return temp


def ignore_wrdsinlst():
    lst = config_commands('config_sw1.txt')
    lst = lst.split('\n')
    for line in lst:
        if not any(ignore_word in line for ignore_word in ignore):
            print(line)


ignore_wrdsinlst()


def config_print(filename=''):
    if filename:
        if check_if_file_exists(filename):
            config_commands(filename)
        else:
            print("No such file")
    else:
        config_commands('config_sw1.txt')


def check_if_file_exists(filename):
    for x in os.listdir('.'):
        if filename in x:
            return True
        else:
            return False


config_print()
