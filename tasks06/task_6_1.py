mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']

mac_cisco = []
for temp in mac:
    temp = temp.replace(':', '.')
    #print(temp)
    mac_cisco.append(temp)

print(mac_cisco)