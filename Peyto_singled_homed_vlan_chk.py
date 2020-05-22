# -*- coding: utf-8 -*-
"""
Created on Mon May 18 09:01:50 2020

@author: Synophic
"""
import telnetlib

peyto_ip = list(map(str, raw_input("Enter a peyto ip's with space : ").split()))

for ip in peyto_ip:
    user = 'amitmal'
    password = 'Bharti@123'
    telnet = telnetlib.Telnet(ip)
    telnet.read_until('username:', 1)
    telnet.write('\n')
    telnet.write(user + '\r')
    telnet.read_until('password:', 1)
    telnet.write(password + '\r')
    telnet.read_until('#')
    telnet.write("ter len 0\n")
    telnet.write("show evpn evi nei\n")
    telnet.write("exit\n")
    output = telnet.read_all()
    new1 = output.splitlines()[11:-2]
    evpn_nei_list = []
    for i in new1:
        Z = i.split('MPLS')[0]
        evpn_nei_list.append(Z.strip())
    telnet = telnetlib.Telnet(ip)
    telnet.read_until('username:', 1)
    telnet.write('\n')
    telnet.write(user + '\r')
    telnet.read_until('password:', 1)
    telnet.write(password + '\r')
    telnet.read_until('#')
    telnet.write("ter len 0\n")
    telnet.write("show arp vrf all\n")
    telnet.write("exit\n")
    output1 = telnet.read_all()
    new2 = output1.splitlines()[13:-2]
    l = []
    for q in new2:
        k = q.split('ARPA')[1]
        g = k.split('BVI')[1]
        l.append(g)
    print('singled homed vlans for '+ ip)
    result = set(l) - set(evpn_nei_list)
    print(result)
    telnet = telnetlib.Telnet(ip)
    telnet.read_until('username:', 1)
    telnet.write('\n')
    telnet.write(user + '\r')
    telnet.read_until('password:', 1)
    telnet.write(password + '\r')
    telnet.read_until('#')
    telnet.write("ter len 0\n")
    telnet.write("sh isis fast-reroute summary\n")
    telnet.write("exit\n")
    output2 = telnet.read_all()
    print(output2)

