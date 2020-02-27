# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 21:24:41 2020

@author: Synophic
"""

# All API calls are leaverged from yang explorer
from ncclient import manager
import xmltodict
import xml.dom.minidom

device = manager.connect(host='192.168.231.111', port=22, username='vikas',
                         password='root', hostkey_verify=False,
                         device_params={'name': 'iosxr'}, allow_agent=False,
                         look_for_keys=False)

# This is get running configuration 
running_config = device.get_config('running')

#print(running_config)

conf_json = str(running_config)

#converting xml to dict
conf_json1 = xmltodict.parse(str(running_config))

#print(conf_json)
# Getting hostanme from running configuration
print(conf_json1['rpc-reply']["data"]["host-names"]["host-name"])

f = open("demofile2.txt", "a")
f.write(conf_json)
f.close()

# this filter to get the configuration of interface
get_filter = """
<interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
     <interface-configuration>
       <interface-name>GigabitEthernet0/0/0/0</interface-name>
     </interface-configuration>
</interface-configurations>
"""


nc_get_reply = device.get(('subtree', get_filter))

A = nc_get_reply
print(A)

# This Filter to create loopback configuration on XR with cisco namespace
get_filter = """
<config>
  <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
     <interface-configuration>
       <active>act</active>
       <interface-name>Loopback200</interface-name>
       <interface-virtual/>
     </interface-configuration>
  </interface-configurations>
</config>
"""
nc_get_reply = device.edit_config(target = 'candidate',config = get_filter)
device.commit()

# This Filter to do bgp configuration on XR with Yang open namespace
get_filter = """
<config>
  <bgp xmlns="http://openconfig.net/yang/bgp">
     <global>
       <config>
         <as>65512</as>
       </config>
     </global>
  </bgp>
</config>
"""
nc_get_reply = device.edit_config(target = 'candidate',config = get_filter)
device.commit()


device.close_session()

