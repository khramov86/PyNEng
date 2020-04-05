

command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

command1vlan = set(command1.split(' ')[4].split(','))
print(command1vlan)

command2vlan = set(command2.split(' ')[4].split(','))
print(command2vlan)
#пересечение множеств
vlan_intersection = command2vlan.intersection(command1vlan)

print(vlan_intersection)
