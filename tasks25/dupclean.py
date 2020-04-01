topology_example = {
    ('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
    ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
    ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
    ('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
    ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
    ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
    ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
    ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
    ('SW1', 'Eth0/3'): ('R3', 'Eth0/0'),
    ('SW1', 'Eth0/2'): ('R2', 'Eth0/0')
}

cleaned_dict = {}
start = True
for key, value in topology_example.items():
    if start:
        cleaned_dict[key] = value
        start = False
    else:
        if key in cleaned_dict.keys() or value in cleaned_dict.keys():
            continue
        else:
            cleaned_dict[key] = value
for key, value in cleaned_dict.items():
    print(key, value)
