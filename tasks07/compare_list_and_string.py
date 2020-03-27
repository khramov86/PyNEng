str = '''

Current configuration : 2033 bytes
!
! Last configuration change at 13:11:59 UTC Thu Feb 25 2016
!
version 15.0
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname sw1
!
!
!
!
! 
!
!
!
!
!
!
interface Ethernet0/0
 duplex auto
!
interface Ethernet0/1
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 switchport mode trunk
 duplex auto
 spanning-tree portfast edge trunk
!
interface Ethernet0/2
 duplex auto
!         
interface Ethernet0/3
 switchport trunk encapsulation dot1q
 switchport trunk allowed vlan 100
 duplex auto
 switchport mode trunk
 spanning-tree portfast edge trunk
!         
interface Ethernet1/0
 duplex auto
!
interface Ethernet1/1
 duplex auto
!
interface Ethernet1/2
 duplex auto
!
interface Ethernet1/3
 duplex auto
!
interface Vlan100
 ip address 10.0.100.1 255.255.255.0
!
!
alias configure sh do sh 
alias exec ospf sh run | s ^router ospf
alias exec bri show ip int bri | exc unass
alias exec id show int desc
alias exec top sh proc cpu sorted | excl 0.00%__0.00%__0.00%
alias exec c conf t
alias exec diff sh archive config differences nvram:startup-config system:running-config
alias exec shcr sh run | s ^crypto
alias exec desc sh int desc | ex down
alias exec bgp sh run | s ^router bgp
alias exec xc sh xconnect all
alias exec vc sh mpls l2tr vc
!
line con 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
line aux 0
line vty 0 4
 login
 transport duplex input all
!
end
'''

ignore = ['duplex', 'alias', 'Current configuration']

for lst in str.split('\n'):
    #print(lst)
    for word in ignore:
        #print(word)
        if lst.strip().find(word) == 0:
             print(lst)
        #     pass



# string =' transport duplex input all'
# if string.find('duplex'):
#     print(string)


#
# for word in ignore:
#     #print(word)
#     print("Trying to find word:\t{}\nin string:\t{}".format(word, list_str))
#     if list_str.find(word):
#         print(list_str)
# # list_str.find(ignore)
