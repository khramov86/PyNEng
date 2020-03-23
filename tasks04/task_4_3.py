config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
listConfig = config.split(' ')
print(listConfig)
vlans = listConfig[4]
vlans = vlans.split(',')

print(set(vlans))
