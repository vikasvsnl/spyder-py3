# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 15:36:37 2019

@author: Synophic
"""

import jinja2
import csv

config = 'config_template.j2'


        
with open(config) as e:
    output = e.read()

csv_file = 'peyto_onboarding.csv'
with open(csv_file) as f:
    read_csv = csv.DictReader(f)
    for bgp_var in read_csv:
        bgp_var
        t = jinja2.Template(output)
        print('#'*80)
        print(bgp_var['circle'] + ' PEYTO_IP ' + bgp_var['Loopback0_IP1'])
        print('#'*80)
        print(t.render(bgp_var))
        file = open('config_file.txt', 'a')
        file.write('#'*80 + "\n")
        file.write(bgp_var['circle'] + ' PEYTO_IP ' + bgp_var['Loopback0_IP1'] + "\n")
        file.write('#'*80 + "\n")
        file.write(t.render(bgp_var))
        file.close()
        
        