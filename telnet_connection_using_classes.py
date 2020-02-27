# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 00:29:52 2020

@author: Synophic
"""
import telnetlib

user = "vikas"
password = "root"

class connection:
    #this is starting connection to router
    def __init__(self, ip):
        self.ip = ip
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b'username: ', 3)
        self.telnet.write(user.encode() + b'\r')
        self.telnet.read_until(b'password: ', 3)
        self.telnet.write(password.encode() + b'\r')
        self.telnet.read_until(b'#')

    # for show commands file /input etc we can use
    def show_commands(self,commands):
        self.telnet.write(b'ter len 0\n')
        for command in commands:
            self.telnet.write(command.encode())
        self.telnet.write(b'exit\n')
        return self.telnet.read_all().decode()
   

# taking class name connection in router variable
router = connection(b'192.168.231.111')
print(router)

commands1 = '''
show ip interface brief
show ospf nei
'''
# calling class name.function under in class for show commands
print(router.show_commands(commands1))