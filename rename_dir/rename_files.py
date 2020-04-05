import os
import subprocess

base_dir = 'C:\\sctretching\\'

# TODO
# Form list of commands to execute the one time

# Function to rename multiple files
def rename():
    # i = 0

    for filename in os.listdir(base_dir):
        # dst = "Hostel" + str(i) + ".jpg"
        # src = 'xyz' + filename
        # dst = 'xyz' + dst

        for i in range(10):
            if filename.startswith(str(i) + '.'):
                newfilename = '0' + filename
                print(filename, newfilename)
                os.rename(base_dir + filename, base_dir + newfilename)

        # rename() function will
        # rename all the files
        # os.rename(src, dst)
        # i += 1


def gen_commands():
    dict = {
        'DAY01': [1, 2, 10, 18, 16, 12, 15]
    }


text = """
ДЕНЬ 1:	1, 2,10,18,16,12,15
ДЕНЬ 16:	1, 2, 3, 4, 7, 9, 8,17,19,12
ДЕНЬ 2:	1, 2,17,11, 4,13,19, 20,25
ДЕНЬ 17:	1, 2, 4,10, 23,15, 5
ДЕНЬ 3:	1, 2, 8, 3, 6,14,21,15
ДЕНЬ 18:	1, 2, 3, 6, 8,15, 21
ДЕНЬ 4:	1, 2, 7,16, 11, 13, 9, 5, 25
ДЕНЬ 19:	1, 2, 4,11,15,16
ДЕНЬ 5:	1, 2, 3, 4, 21,12,14,15
ДЕНЬ 20:	1, 2, 5,13,15, 22, 3
ДЕНЬ 6:	1, 2, 8,10,14,18,11,19, 20, 24
ДЕНЬ 21:	1, 2,10,11,15,18
ДЕНЬ 7:	1, 2, 7, 5, 8,12,17, 22, 21, 23
ДЕНЬ 22:	1, 2,14,12,19,15,16
ДЕНЬ 8:	1, 2, 4, 5,10, 6,11,16, 21, 22, 25
ДЕНЬ 23:	1, 2,10, 3, 7, 4, 6, 21, 22, 23
ДЕНЬ 9:	1, 2, 3, 7, 8, 9,13,12,19,18, 24
ДЕНЬ 24:	1, 2, 3, 8,13,12,18, 24, 23
ДЕНЬ 10:	1, 2, 23,10,11,16,14,19, 20, 22
ДЕНЬ 25:	1, 2, 4, 9,14,19, 20, 25, 21
ДЕНЬ 11:	1, 2, 3,10,17, 21,15
ДЕНЬ 26:	1, 2, 8, 6,13,18,19, 22, 24, 23
ДЕНЬ 12:	1, 2, 9,12,18,15
ДЕНЬ 27:	1, 2, 9,10,14,18, 20, 21, 25
ДЕНЬ 13:	1, 2, 4, 7, 6, 23,17,16,13,14
ДЕНЬ 28:	1, 2,19, 20, 8, 6, 5,12, 24, 25
ДЕНЬ 14:	1, 2, 3, 5, 8, 9,19,17,18, 25
ДЕНЬ 29:	1, 2, 9,12,19, 20,18, 24, 25
ДЕНЬ 15:	1, 2,12,11,14,17,19, 20, 24
ДЕНЬ 30:	1, 2,19, 20, 24, 25, 22,15

"""


def parse_text():
    dct = {}
    gen_commands()
    for line in text.strip().split('\n'):
        if line.rstrip('\\t').split(':')[1].startswith('\t'):
            temp = line.strip('\t').split(':')[1]
            for i in range(10):
                if line.split(':')[0].endswith(' ' + str(i)):
                    dct[line.split(':')[0][:5] + '0' + line.split(':')[0][5:]] = temp.strip('\t').strip(' ')
            else:
                for i in range(10, 100):
                    if line.split(':')[0].endswith(' ' + str(i)):
                        dct[line.split(':')[0]] = temp.strip('\t').strip(' ')
        else:
            dct[line.split(':')[0]] = line.rstrip().split(':')[1]
    return dct


def remove_symls(dct):
    tempdict = {}
    for key, value in sorted(dct.items()):
        temp = ''
        for i in value.split(","):
            # print(i.strip(' '))
            if int(i.strip(' ')) in range(10):
                temp += '\nfile \'' + '0' + i.strip(' ') + '.mp4\'' + ' ' + '\nfile \'pause.mp4\''
            else:
                temp += '\nfile \'' + i.strip(' ') + '.mp4\'' + ' ' + '\nfile \'pause.mp4\''

        tempdict[key] = temp
    return tempdict


def command_form():
    com = remove_symls(parse_text())
    for key, val in com.items():
        print("ffmpeg -f concat -safe 0 -i < \"{}\" -c copy {}".format(val + '\n', 'Day' +key[5:] +'.mp4'))

command_form()

# if __name__ == '__main__':
#     main()
