# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 09:51:12 2020

@author: Synophic
"""

import ipaddress

class subnet_calculator:
    def __init__(self, network):
        self.network = network
        self.net = ipaddress.IPv4Network(network)

    # Test if an IP is in the subnet
    def ip_in_subnet(self, ip):
        if ipaddress.IPv4Address(ip) in list(self.net.hosts()):
            return True
        else:
            return False
    
    # Is my network part of another network
    def my_net_to_another(self, network):
        if self.net.overlaps(ipaddress.IPv4Network(network)):
            return True
        else:
            return False

    # DNS PTR Record from IP
    # note the staticmethod without self in method
    @staticmethod
    def ip_to_ptr(ip):
        return ipaddress.ip_address(ip).reverse_pointer
   

net1 = subnet_calculator('1.1.1.0/24')
print(net1.network)

print(net1.ip_in_subnet('192.168.1.1'))

print(net1.my_net_to_another('192.168.1.0/30'))

print(subnet_calculator.ip_to_ptr('1.1.1.1'))