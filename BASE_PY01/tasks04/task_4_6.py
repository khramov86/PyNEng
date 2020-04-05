import re
import pprint
ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_route = re.split(r' +', ospf_route)
ospf_route.remove('via')
ospf_route[2].replace('[','')
ospf_route[2].replace(']','')
print(ospf_route)
metrics = ['Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']

print(metrics)
emptyDict = {}
for i in range(0, len(ospf_route)):
    emptyDict[metrics[i]] = ospf_route[i]


pprint.pprint(emptyDict)
# for key in emptyDict.keys():
#      pprint(key + " \t : \t" + emptyDict[key])


