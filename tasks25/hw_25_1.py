import tasks25.dupclean as dups
class Topology:
    def __init__(self, topology):
        self.topology = topology

    def remove_duplicates(self):
        print(self.topology)
        print(dups.clean_dups(self.topology))

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
