# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 18:29:27 2020

@author: Synophic
"""

import telnetlib


print('''This python script is for the Services migration activity which will shutdown the
      BE on the T3/ASR9K routers and will enable the BVI on Peyto's give by you in input''' )

dict1 = {}
peyto_list = list(map(str, raw_input("Enter a T3 ip's with space : ").split()))
dict2 = {}

for T3 in peyto_list:
    #dict1['BE'] = list(map(str, input("Enter a BE number with space for " + T3 +"  : ").split()))
    dict1[T3] = list(map(str, raw_input("Enter a BEID like(BE101) and vlan number with space like( 1 2 3) for " + T3 +"  : ").split()))   

print(dict1)

peyto_list1 = list(map(str, raw_input("Enter a Peyto ip's with space : ").split()))

for T3,vlans in dict1.items():
    BE = vlans[0]
    print('Configurations for T3 router = ' + T3 + ' **************************')
    print('************Below configuartion will pushed now to router***********************')
    for vlan in vlans[1:]:
        port = str(BE) + '.' + str(vlan)
        print("interface " + port)
        print("shutdown")
        
action = raw_input('Enter yes if you want to Proceed Further: ')

if action == 'yes':
    for T3,vlans in dict1.items():
        BE = vlans[0]
        print(T3)
        user = "Y2lzY29pbg==".decode('base64')
        password = "QmhhcnRpQDEyMw==".decode('base64')
        telnet = telnetlib.Telnet(T3)
        telnet.read_until('username: ', 3)
        telnet.write(user + '\r')
        telnet.read_until('password: ', 3)
        telnet.write(password + '\r')
        telnet.read_until('#')
        telnet.write("conf terminal\n")
        for vlan in vlans[1:]:
            port = str(BE) + '.' + str(vlan)
            telnet.write("do sh arp vrf all | include  " + port + "\n")
            telnet.write("interface " + port + "\n")
            telnet.write("shutdown\n")
            telnet.write("root\n")
        telnet.write("commit\n")
        telnet.write("exit\n")
        telnet.write('ter len 0\n')
        telnet.write("sh interfaces description\n")
        telnet.write("exit\n")
        output = telnet.read_all()
        print(output)
        
    for peyto in peyto_list1:
        print(peyto)
        user = "c2hpczAwMjA=".decode('base64')
        password = "U3VuaWxAMDA=".decode('base64')
        telnet = telnetlib.Telnet(peyto)
        telnet.read_until('username: ', 3)
        telnet.write(user + '\r')
        telnet.read_until('password: ', 3)
        telnet.write(password + '\r')
        telnet.read_until('#')
        telnet.write("conf terminal\n")
        for vlan in vlans[1:]:
            port = 'BVI' + str(vlan)
            telnet.write("interface " + port+ "\n")
            telnet.write("no shutdown\n")
            telnet.write("root\n")
        telnet.write("commit\n")
        telnet.write("exit\n")
        telnet.write('ter len 0\n')
        telnet.write("sh interfaces description\n")
        telnet.write("exit\n")
        output = telnet.read_all()
        print(output)
        