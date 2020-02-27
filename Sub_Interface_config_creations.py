# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 21:08:14 2020

@author: Synophic
"""

import jinja2
import csv

config = 'Sub_interface_template.j2'


        
with open(config) as e:
    output = e.read()

csv_file = 'Sub_interface_creation_variables.csv'
with open(csv_file) as f:
    read_csv = csv.DictReader(f)
    for var in read_csv:
        var
        t = jinja2.Template(output)
        #print(var['circle'] + ' PEYTO_IP ' + var['Loopback0_IP1'])
        print('#'*80)
        #print(t.render(var))
        file = open(var['loopback_ip'] + '.txt', 'w')
        file.write(t.render(var))
        file.close()