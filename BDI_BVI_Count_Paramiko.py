# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 08:32:44 2020

@author: Synophic
"""

import paramiko
import time

user = "test"
password = "test"

#peyto = raw_input('Enter peyto IP: ')

class connection:
    #this is starting connection to router
    def __init__(self, ip):
        self.ip = ip
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname=ip,username=user,password=password,look_for_keys=False, allow_agent=False)
        #self.ssh_client.invoke_shell()
    # for show commands file /input etc we can use
    def show_commands(self,commands):
        router_conn = self.ssh_client.invoke_shell()
        time.sleep(1)
        router_conn.send("ter len 0\n")
        output = router_conn.recv(65535)
        #print(output)
        for command in commands:
            router_conn.send(command)
            time.sleep(1)
        output1 = router_conn.recv(6553500)
        return output1
#file4 = open('bd_output' + '.csv','a')
commands1 = open('peyto.txt','r')
# taking class name connection in router variable
for peyto in commands1:
   try:
      router = connection(peyto)
      BVI = "sh interfaces summary | i IFT_BVI\n"
      output = router.show_commands(BVI)
      new2 = output.splitlines()
      new3 = str(new2[-2])
      #print(type(new3))
      new4 = new3.split()[1:3]
      print(new4)
      #file4.write(new4)
      router = connection(peyto)
      BD = "sh l2vpn bridge-domain summary | i bridge-domains\n"
      output = router.show_commands(BD)
      new1 = str(output.splitlines()[-2])
      new7 = new1.split()[3:6]
      print(new1)
      file4 = open('bd_output' + '.csv','a')
      file4.write(peyto + ' Total_INF_BVI ' + new4[0] + ' UP_BVI '+ new4[1] + ' Total_BD ' + new7[0] + ' UP_BD '  + new7[2])
      file4.close()
   except Exception:
        print(peyto + 'Please check you IP and Enter correct IP or Device is unreachable/Down')
