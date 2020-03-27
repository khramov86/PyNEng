str = '''
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
Current configuration : 2033 bytes
'''

ignore = ['duplex', 'alias', 'Current configuration']

for list in str.split('\n'):
    print(list)


#
# for word in ignore:
#     #print(word)
#     print("Trying to find word:\t{}\nin string:\t{}".format(word, list_str))
#     if list_str.find(word):
#         print(list_str)
# # list_str.find(ignore)
