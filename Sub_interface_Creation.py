# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 15:33:36 2020

@author: Vikas Sehgal
"""

import telnetlib
import time
import re
import base64

regex = r"rate \d+"
telnet = None
T3_IP = input('Enter T3 IP: ')
BE_number = input('Enter BE number: ')

user = base64.b64decode("dmlrYXM=").decode("utf-8")
password = base64.b64decode("cm9vdA==").decode("utf-8")

config_1 = (T3_IP + '_1.txt')
def Function1(): #for connection only
    global telnet
    telnet = telnetlib.Telnet(T3_IP)
    telnet.read_until(b'username: ', 3)
    telnet.write(user.encode('ascii') + b'\r')
    telnet.read_until(b'password: ', 3)
    telnet.write(password.encode('ascii') + b'\r')
    telnet.read_until(b'#')

def Function2(): # Pre & Post Checks
    telnet.write(b"sh running-config router isis IGP interface bundle-ether" + BE_number.encode('ascii') + b"\n")
    telnet.write(b"show interface bundle-ether" + BE_number.encode('ascii') + b" | i rate\n")
    telnet.write(b"ter len 0\n")
    telnet.write(b"show isis nei detail\n")
    telnet.write(b"show bgp all all summary\n")
    telnet.write(b"show mpls ldp nei\n")
    telnet.write(b"show pim nei\n")
    telnet.write(b"show mpls ldp nei | i Up\n")
    telnet.write(b"show platform\n")
    telnet.write(b"show logging last 100\n")
    telnet.write(b"exit\n")
    print(telnet.read_all().decode('ascii'))


def Function5(): #Call to execute command 1 for increasing metric
    telnet.write(b"conf terminal\n")
    telnet.write(b"router isis IGP\n")
    telnet.write(b"interface Bundle-Ether" + BE_number.encode('ascii') +b"\n")
    telnet.write(b"address-family ipv4 unicast\n")
    telnet.write(b"metric 1600000 level 2\n")
    telnet.write(b"root\n")
    telnet.write(b"commit\n")
    telnet.write(b"exit\n")
    print(time.ctime())
    n = 25
    i = 0
    while i < n:
        i = i + 5
        time.sleep(10)
        telnet.write(b"sh interfaces be10 | i rate\n")
    telnet.write(b"exit\n")
    output = telnet.read_all().decode('ascii')
    print(output)
    matches = re.finditer(regex, output, re.MULTILINE)
    for match in matches:
        print(match)
Function1() #Call for telnet connection
Function2() # Pre & Post Checks
Function1() #Call for telnet connection
Function5() #Call to execute command 1 for increasing metric

Action = input('Enter yes to proceed further: ')

def Function3(): # Call to check traffic on BE interface
    telnet.write(b"sh interfaces be10 | i rate\n")
    telnet.write(b"exit\n")
    output = telnet.read_all().decode('ascii')
    print(output)
    matches = re.finditer(regex, output, re.MULTILINE)
    for match in matches:
        print(match)
        
def Function4():# This function will be called once you yes and config will be pushed to device
    telnet.write(b"conf terminal\n")
    telnet.write(output1.encode())
    telnet.write(b"commit\n")
    telnet.write(b"root\n")
    telnet.write(b"exit\n")
    telnet.write(b"exit\n")
    output = telnet.read_all().decode('ascii')
    print(output)

while Action != 'yes':
    Function1()
    Function3()
    Action = input('Enter yes to proceed further: ')
    
if Action == 'yes':
    config_2 = (T3_IP + '_2.txt')
    with open(config_2) as e:
        output1 = e.read()
    Function1()
    Function4()
    
Function1()
Function2()

