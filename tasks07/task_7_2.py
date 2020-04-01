"""
To dowload file
wget --no-check-certificate https://raw.githubusercontent.com/natenka/pyneng-examples-exercises/master/exercises/07_files/config_sw1.txt
author Vladimir Khramov

"""
import os

filename = input("Введите имя файла ")

ignore = ['duplex', 'alias', 'Current configuration']


def config_commands(filename):
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('!'):
                continue
            elif alg_check(line):
                continue
            else:
                print(line)


def config_print():
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


#

def alg_check(str):
    # for word in ignore:
    elements = str.split()
    for element in elements:
        if element in ignore:
            #   print(element + " Ignored")
            return True
            break
    #        else:
    # print(element + " Not ignored")
    return False


#
# if alg_check("spanning-tree portfast edge trunk"):
#     print("string ignored")
# config_print()


def alg_check_andr():
    for s in str.split("\n"):
        if [word for word in ignore if word in s]:
            print(s)
