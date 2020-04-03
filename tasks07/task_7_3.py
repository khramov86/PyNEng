
vlan = input('Введите vlan: ')

def open_file(filename, vlan):
    with open(filename, 'r', encoding='utf8') as f:
        notinflines = True
        for line in f:

            if notinflines:
                if line.startswith('----    -----------       --------    -----'):
                    notinflines = False
            else:
                # print("compare string with vlan")
                # print("string is {}.".format(line.strip().split('   ')[0]))
                # print("vlan is {}".format(vlan))
                if line.strip().split('   ')[0].strip() == str(vlan):
                    print(line.strip().split('   ')[0].split() + line.strip().split('   ')[1].split() + line.strip().split('   ')[3].split())


if __name__ == '__main__':
    open_file('CAM_table.txt', vlan)
