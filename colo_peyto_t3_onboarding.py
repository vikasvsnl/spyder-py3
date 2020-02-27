# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 21:24:06 2020

@author: Synophic
"""



import getpass
import sys
import telnetlib
import time
import re

user = "Y2lzY29pbg==".decode('base64')
password = "QmhhcnRpQDEyMw==".decode('base64')

new_dict = {}

T3_A = raw_input("Enter First T3 IP: ")

T3_B = raw_input("Enter Second T3 IP: ")

new_dict['Peyto_hostname'] = raw_input("Enter Peyto hostname: ")
new_dict['Peyto_hostname'] = new_dict['Peyto_hostname'].upper()
new_dict['Peyto_IP'] = raw_input("Enter peyto IP: ")



#print(new_dict['Peyto_hostname'])

list1 = [T3_A, T3_B]


new_list = []
for T3 in list1:

    telnet = telnetlib.Telnet(T3)
    telnet.read_until('Username: ', 3)
    telnet.write(user + "\n")
    telnet.read_until('Password: ', 3)
    telnet.write(password + "\n")
    telnet.read_until('#')
    telnet.write("sh running-config formal | include "+ new_dict['Peyto_hostname'] + "\n")
    telnet.write("exit\n")
    output = telnet.read_all()
    #print(output)
    output1 = output.splitlines()
    for line in output1:
        if new_dict['Peyto_hostname'] and 'Bundle-Ether' in line:
            print(line)
            C = line.split()[1]
            new_list.append(C)

print(new_list)

ipv6_list = []

for (BE,T3) in zip(new_list,list1):
    print("*****************Before config push*****************")
    telnet = telnetlib.Telnet(T3)
    telnet.read_until('Username: ', 3)
    telnet.write(user + "\n")
    telnet.read_until('Password: ', 3)
    telnet.write(password + "\n")
    telnet.read_until('#')
    telnet.write("ter len 0\n")
    telnet.write("show run int " + BE + "\n")
    telnet.write("show run router isis T4 interface "+  BE + "\n")
    telnet.write("show run router bgp 9730 nei  " + new_dict['Peyto_IP'] + "\n")
    telnet.write("show logging last 20\n")
    telnet.write("exit\n")
    output = telnet.read_all()
    print(output)
    output1 = output.splitlines()
    for line in output1:
        if 'ipv4 address ' in line:
            print('-'*80)
            print("Configured IPV4 Address on " + T3 )
            print(line)
            ipv4 = line.split(' ')[3]
            ipv4 = ipv4.split('.')
            string = ':'
            string = string.join(ipv4)
            ipv6_addresses = '2404:a800:0:2c:'+ string + '/127'
            ipv6_list.append(ipv6_addresses)
            print('Derived ipv6 address from ipv4 address for ' + T3 )
            print(ipv6_addresses)
            print('-'*80)
print(ipv6_list)

template="""interface {BE1}
 bfd mode ietf
 bfd address-family ipv4 timers start 60
 bfd address-family ipv4 multiplier 3
 bfd address-family ipv4 fast-detect
 bfd address-family ipv4 minimum-interval 50
 mtu 9216
 service-policy output CORE-MPLS-ASR9k-BHARTI_NEW
 ipv6 address {IPv6_Address}
 load-interval 30
!

router isis T4
 interface {BE1}
  circuit-type level-2-only
  point-to-point
  hello-padding disable
  hello-password keychain bharti
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa


router bgp 9730
 neighbor {Peyto_IP}
 use neighbor-group T4-CRR

lpts punt excessive-flow-trap  exclude interface {BE1}

"""


generatedconfig=template.replace("{BE1}",new_list[0])
generatedconfig1=generatedconfig.replace("{IPv6_Address}",ipv6_list[0])
T3_A_Onboarding=generatedconfig1.replace("{Peyto_IP}",new_dict['Peyto_IP'])

print('#' * 50)
print("configuration for " + list1[0] )
print('#' * 50)
print(T3_A_Onboarding)
print('\n')
sec_generatedconfig=template.replace("{BE1}",new_list[1])
sec_generatedconfig1=sec_generatedconfig.replace("{IPv6_Address}",ipv6_list[1])
T3_B_Onboarding=sec_generatedconfig1.replace("{Peyto_IP}",new_dict['Peyto_IP'])
print('#' * 50)
print("configuration for " + list1[1] )
print('#' * 50)
print(T3_B_Onboarding)
print('#' * 50)

onboarding = [T3_A_Onboarding, T3_B_Onboarding]

action = raw_input("Please let me know if you want to proceed for configuration, type yes : ")
if action == 'yes':
    for (T3, onboarding1) in zip(list1 ,onboarding):
        telnet = telnetlib.Telnet(T3)
        telnet.read_until('Username: ', 3)
        telnet.write(user + "\n")
        telnet.read_until('Password: ', 3)
        telnet.write(password + "\n")
        telnet.read_until('#')
        telnet.write("conf t\n")
        telnet.write(onboarding1)
        telnet.write("root\n")
        telnet.write("commit\n")
        telnet.write("exit\n")
        telnet.write("exit\n")
        output = telnet.read_all()
        #print(output)



for (BE,T3) in zip(new_list,list1):
    print("*****************After config push*****************")
    telnet = telnetlib.Telnet(T3)
    telnet.read_until('Username: ', 3)
    telnet.write(user + "\n")
    telnet.read_until('Password: ', 3)
    telnet.write(password + "\n")
    telnet.read_until('#')
    telnet.write("ter len 0\n")
    telnet.write("show run int " + BE + "\n")
    telnet.write("show run router isis T4 interface "+  BE + "\n")
    telnet.write("show run router bgp 9730 nei  " + new_dict['Peyto_IP'] + "\n")
    telnet.write("show logging last 20\n")
    telnet.write("exit\n")
    output = telnet.read_all()
    print(output)
