# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:26:54 2020

@author: Synophic
"""

import re
import telnetlib

T3_A_IP = raw_input('Enter First T3 IP (Loopback IP): ')
T3_B_IP = raw_input('Enter Second T3 IP (Loopback IP): ')
T3_A_port = raw_input('Enter First T3 Port number as per plan e.g. 0/0/1/1:' )
T3_B_port = raw_input('Enter Second T3 Port number as per plan e.g. 0/0/1/1:' )
T3_A_int_IP = raw_input('Enter First T3 interface IP as per plan: ')
T3_B_int_IP = raw_input('Enter Second T3 interface IP as per plan: ')
T3_A_BE1 = raw_input('Enter First T3 Bundle number you will use e.g 104 or 105: ')
T3_B_BE2 = raw_input('Enter Second T3 Bundle number you will use e.g 104 or 105 : ')

T3_L0_IP = [T3_A_IP,T3_B_IP ]
T3_port = [T3_A_port, T3_B_port]
T3_int_IP = [T3_A_int_IP, T3_B_int_IP]
T3_BE = [T3_A_BE1,T3_B_BE2]
location = []
for port in T3_port:
    b = port.split('/')
    list1 = b[0] + '/' + b[1] + '/cpu0'
    location.append(list1)

for (Loopback_ip,port,int_ip,hw_location,bundle) in zip(T3_L0_IP,T3_port,T3_int_IP,location,T3_BE):
    user = "Y2lzY29pbg==".decode('base64')
    password = "QmhhcnRpQDEyMw==".decode('base64')
    telnet = telnetlib.Telnet(Loopback_ip)
    telnet.read_until('Username: ', 3)
    telnet.write(user + '\r')
    telnet.read_until('Password: ', 3)
    telnet.write(password + '\r')
    telnet.read_until('#')
    telnet.write("ter len 0\n")
    telnet.write("show int hu" + port + "\n")
    telnet.write("show run int bundle-ether " + bundle + "\n")
    telnet.write("show route " + int_ip + "\n" )
    telnet.write("show platform\n")
    telnet.write("sh interfaces description location " + hw_location + "\n")
    telnet.write("exit\n")
    output = telnet.read_all()
    print(output)
    output1 = output.splitlines()
    for line in output1:
        if 'line protocol is up' in line:
            print('#')*80
            print('Please do not proceed further as interface is used')
            print('#')*80
        #if 'No such configuration item(s)' in line:
            print('#')*80
            print('Please proceed further,Bundle is unused')
            print('#')*80
        if 'interface Bundle-Ether' in line:
            print('#')*80
            print('Please do not proceed further as Bundle is in used')
            print('#')*80
        #if 'line protocol is administratively down' in line:
            print('#')*80
            print('Please proceed further,interface is unused')
            print('#')*80
        if "Routing entry for " in line:
            print('#')*80
            print('Please Do not proceed further,IP is used')
            print('#')*80
