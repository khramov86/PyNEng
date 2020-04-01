class Topology:
    def __init__(self, topology):
        self.topology = topology

    def remove_duplicates(self):
       # print(self.topology)
        temp_dict = {}
        for key, value in self.topology.items():
           # print(key, value)
           # добавить один элемент
            if temp_dict:
                temp_dict[key] = value
             #   print(temp_dict)
            else:
                if key in temp_dict.keys():

                    print("There is such key or value")
                elif key in temp_dict.values():
                        print("There is such key or value")
                else:
                    temp_dict[key] = value
               # print(temp_dict)
            # else:
            #     if temp_dict[key] != self.topology_example[key]:
            #         continue
            #     else:
            #         temp_dict[key] = value
            # else:
            #     if topology_example[key] == temp_dict[key]:
            #         continue
            #     elif topology_example[value] == temp_dict[key]:
            #         continue
            #     else:
            #         temp_dict[key] = value
        for key,value in temp_dict.items():
            print(key, value)




"""Дублем считается ситуация, когда в словаре есть такие пары: ('R1', 'Eth0/0'): ('SW1', 'Eth0/1')
 и ('SW1','Eth0/1'): ('R1', 'Eth0/0') """

topology_example = {
                    ('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
                    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
                    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
                    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
                    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
                    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
                    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
                    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
                    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0')}

top = Topology(topology_example)
top.remove_duplicates()
