# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 15:40:19 2019
"""
import getpass
import sys
import telnetlib
import time
import re

A = []
host = raw_input('Enter Source IP: ')
Dest = raw_input('Enter Destination IP: ')

#print(A)

while A != '(connected)':
    user = 'amitmal'
    password = 'Bharti@123'
    telnet = telnetlib.Telnet(host)
    
    
    telnet.read_until('username: ', 3)
    telnet.write(user + '\r')
    telnet.read_until('password: ', 3)
    telnet.write(password + '\r')
    telnet.read_until('#')
    telnet.write("ter len 0\n")
    telnet.write("show route " + Dest + "\n")
    telnet.write("exit\n")
    Output3 = telnet.read_all()
    D = Output3.splitlines()
    print(D)
    for line in D:
        if 'Protected' in line:
    
            A = line.split()[4].strip(',')
            (line.split()[5])
            

    telnet = telnetlib.Telnet(host)
    telnet.read_until('username: ', 3)
    telnet.write(user + '\r')
    telnet.read_until('password: ', 3)
    telnet.write(password + '\r')
    telnet.read_until('#')
    telnet.write("ter len 0\n")
    telnet.write("show isis nei " + str(A) + "\n")
    telnet.write("exit\n")
    Output1 = telnet.read_all()
    print(Output1)
    
    Z = Output1.splitlines()
    #print(Z)
    
    for line in Z:
        if 'BE' in line:
            S = line.split()[0]
            telnet = telnetlib.Telnet(host)
            telnet.read_until('username: ', 3)
            telnet.write(user + '\r')
            telnet.read_until('password: ', 3)
            telnet.write(password + '\r')
            telnet.read_until('#')
            telnet.write("ter len 0\n")
            telnet.write("sh isis database " +  S +".00-00 detail" + "\n")
            telnet.write("exit\n")
            Output = telnet.read_all()
            print(Output)
    Z1 = Output1.splitlines()
    #print(Z1)
    for line in Z1:
        if 'MPL-LTE-PE'in line:
            print(line.split()[0])
            telnet = telnetlib.Telnet(host)
            telnet.read_until('username: ', 3)
            telnet.write(user + '\r')
            telnet.read_until('password: ', 3)
            telnet.write(password + '\r')
            telnet.read_until('#')
            telnet.write("ter len 0\n")
            telnet.write("sh isis database " +line.split()[0] +".00-00 detail" + "\n")
            telnet.write("exit\n")
            Output = telnet.read_all()
            print(Output)
        Z = Output.splitlines()
        print(Z)
    for line in Z:
        if 'IP Address:' in line:
                    host = line.split(':')[1].strip()
                    telnet = telnetlib.Telnet(host)
                    telnet.read_until('username: ', 3)
                    telnet.write(user + '\r')
                    telnet.read_until('password: ', 3)
                    telnet.write(password + '\r')
                    telnet.read_until('#')
                    telnet.write("ter len 0\n")
                    telnet.write("show route " + Dest + "\n")
                    telnet.write("exit\n")
                    Output = telnet.read_all()
                    print(Output)
            
    if 'MPL-LTE-PE'in S:
                host_new = S
                B1 = host_new.split('RTR')
                D = (B1[1].split('-'))
                thrird = D[1]
                Fourth = D[2]
                host =  '202.123.'+ thrird + '.' + Fourth
                telnet = telnetlib.Telnet(host)
                user = 'ciscoin'
                password = 'Bharti@123'
                telnet.read_until('Username: ', 3)
                telnet.write(user + '\r')
                telnet.read_until('Password: ', 3)
                telnet.write(password + '\r')
                telnet.read_until('#')
                telnet.write("ter len 0\n")
                telnet.write("show route " + Dest + "\n")
                telnet.write("exit\n")
                Output = telnet.read_all()
                print(Output)
    print(S)
    
    if '(connected)' in Output:
        print('found')
        break
        
    

        
    
    

    
