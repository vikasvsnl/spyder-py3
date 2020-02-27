# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 20:33:25 2020

@author: Synophic
"""
import getpass
import sys
import telnetlib
import time
import re

user = "YW1pdG1hbA==".decode('base64')
password = "QmhhcnRpQDEyMw==".decode('base64')

peyto_list = list(map(str, raw_input("Enter a peyto ip's with space : ").split()))
#print(peyto_list)
T3_list = list(map(str, raw_input("Enter a T3 ip's with space : ").split()))
#print(T3_list)
CMR_list = list(map(str, raw_input("Enter CMR number in order peyto  : ").split()))
#print(CMR_list)

count = 0


for (peyto,CMR) in zip(peyto_list,CMR_list):
    count+= 1
    telnet = telnetlib.Telnet(peyto)
    telnet.read_until('username: ', 3)
    telnet.write(user + '\r')
    telnet.read_until('password: ', 3)
    telnet.write(password + '\r')
    telnet.read_until('#')
    telnet.write("ter len 0\n")
    telnet.write("show isis nei\n")
    telnet.write("sho arp | include Dynamic\n")
    telnet.write("exit\n")
    Output = telnet.read_all()

    Z = re.split(r'\s',Output)

    S = []

    for result in Z:
        f = re.match("BE\w+",result)
        if f:
            g = f.group(0)
            f = S.append(g)
    #print(S)
    # finding IP for ping

    regex = r"^\d+.\d+.\d+.\d+  "

    matches = re.finditer(regex, Output, re.MULTILINE)

    ping = []

    for match in matches:
        ping.append(match.group())

    #print(ping)

    telnet = telnetlib.Telnet(peyto)
    telnet.read_until('username: ', 3)
    telnet.write(user + '\r')
    telnet.read_until('password: ', 3)
    telnet.write(password + '\r')
    telnet.read_until('#')
    telnet.write("ter len 0\n")
    for BE in S:
        telnet.write("sh bun  " + BE + " | i Hu" + "\n")
    telnet.write("exit\n")
    Output1 = telnet.read_all()

    Z1 = re.split(r'\s',Output1)

    S1 = []

    gig_pattern = re.compile('([0-9]\/[0-9]\/[0-9]\/[0-9])')

    for result1 in Z1:
        f = gig_pattern.search(result1)

        if f:
            g = f.group(0)
            S1.append(g)
    #print (S1)



    telnet = telnetlib.Telnet(peyto)
    telnet.read_until('username: ', 3)
    telnet.write(user + '\r')
    telnet.read_until('password: ', 3)
    telnet.write(password + '\r')
    telnet.read_until('#')
    telnet.write("ter len 0\n")
    telnet.write("show isis nei\n")
    telnet.write("show bgp ipv4 labeled-unicast 10.3.135.32/27\n")
    telnet.write("show int des | i " + CMR + "\n")
    telnet.write("show platform\n")
    telnet.write("show install active summary | include Active\n")
    telnet.write("show alarms brief system active\n")
    telnet.write("show install committed summary | include Committed\n")
    telnet.write("show version\n")
    telnet.write("show ntp associations\n")
    telnet.write("show track\n")
    telnet.write("sh bgp ipv4 labeled-unicast summary | b Neighbor" + "\n")
    for BE in S:
        telnet.write("sh bun  " + BE + " | include Hu\n")
    for optics in S1:
        telnet.write("sho controller optics " + optics + " summary\n")
        telnet.write("sho controller optics " + optics + " | include Optical" +"\n")
        telnet.write("show controllers COherentDSP " + optics + " | include BER "+ "\n")
    telnet.write("show inventory\n")
    for ip in ping:
        telnet.write("ping " + ip.strip() + " repeat 1000\n")
    telnet.write("exit\n")
    print('-'*80)
    print(str(count) + " FOR PEYTO " + peyto)
    print('-'*80)
    print (telnet.read_all())


dict1 = dict(zip(CMR_list,T3_list))



print('*********************T3 Router outputs***************************')

for num1,i in enumerate(CMR_list):
    #print(list1[num1])
    if num1 == 0:
        list_1 = []
        list_1.append((T3_list[num1]))
        list_1.append((T3_list[num1+1]))

    else:
        list_1 =[]
        list_1.append(T3_list[num1+num1])
        list_1.append(T3_list[num1+num1+1])

    for ip in list_1:
        CMR = CMR_list[num1]
        user = "ciscosj"
        password = "Bharti@123"
        telnet = telnetlib.Telnet(ip)
        telnet.read_until('username: ', 3)
        telnet.write(user + '\r')
        telnet.read_until('password: ', 3)
        telnet.write(password + '\r')
        telnet.read_until('#')
        telnet.write("show int des | i " + CMR + "\n")
        telnet.write("show ipv4 access-list 65 | i 116.119.0.0\n")
        telnet.write("sh run router bgp 9730 ibgp policy out enforce-modifications\n")
        telnet.write("exit\n")
        print (telnet.read_all())

    

    



    
