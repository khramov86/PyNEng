# При записи, очень важно определиться с режимом открытия файла, чтобы случайно его не удалить:
#
# w - открыть файл для записи. Если файл существует, то его содержимое удаляется
# a - открыть файл для дополнения записи. Данные добавляются в конец файла

cfg_lines = ['!',
             'service timestamps debug datetime msec localtime show-timezone year',
             'service timestamps log datetime msec localtime show-timezone year',
             'service password-encryption',
             'service sequence-numbers',
             '!',
             'no ip domain lookup',
             '!',
             'ip ssh version 2',
             '!']

f = open('r2.txt', 'a')
# Преобразуем список команд в одну большую строку с помощью join:
cfg_lines_as_string = '\n'.join(cfg_lines)
# запишем всё в файл
f.write(cfg_lines_as_string)
f.close()

#Метод writelines() ожидает список строк, как аргумент.

f = open('r2.txt', 'w')
#всё запишется в одну строку
f.writelines(cfg_lines)
f.close()

# чтобы добавить перевод строки можно производить запись следующим образом

cfg_lines2 = []

for line in cfg_lines:
    cfg_lines2.append(line + '\n')

f = open('r2.txt', 'w')
f.writelines(cfg_lines2)
f.close()


