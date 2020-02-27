# -*- coding: utf-8 -*-

import jinja2
import csv

csv_file = 'peyto_onboarding.csv'
with open(csv_file) as f:
    read_csv = csv.DictReader(f)
    #print(read_csv)
    for bgp_var in read_csv:
        read_csv

        
config = 'config_template.j2'
        
with open(config) as e:
    output = e.read()
    #print(output)
    t = jinja2.Template(output)
    print(t.render(bgp_var))