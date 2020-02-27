# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:33:09 2020

@author: Synophic
"""

import telnetlib
dict1 = {}
peyto_list = list(map(str, raw_input("Enter a peyto ip's with space : ").split()))

for peyto in peyto_list:
    dict1[peyto] = list(map(str, raw_input("Enter a port number with space for " + peyto +"  : ").split()))

#print(dict1)

for ip ,ports in dict1.items():
    user = "c2hpczAwMjA=".decode('base64')
    password = "U3VuaWxAMDA=".decode('base64')
    telnet = telnetlib.Telnet(ip)
    telnet.read_until('username: ', 3)
    telnet.write(user + '\r')
    telnet.read_until('password: ', 3)
    telnet.write(password + '\r')
    telnet.read_until('#')
    telnet.write("conf terminal\n")
    for port in ports:
        telnet.write("interface " + port+ " \n")
        telnet.write("no shutdown\n")
    telnet.write("root\n")
    telnet.write("commit\n")
    telnet.write("exit\n")
    telnet.write('ter len 0\n')
    telnet.write("sh interfaces description\n")
    telnet.write("exit\n")
    output = telnet.read_all()
    print(output)
