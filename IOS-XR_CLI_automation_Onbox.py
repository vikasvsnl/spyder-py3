# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 17:06:01 2020

@author: Synophic
"""

#!/usr/bin/env python

'''IOS-XR CLI automation - Bash'''

# more details are avilable on below link for on box scripting

# https://developer.cisco.com/learning/lab/01-iosxr-01-cli-automation-bash/step/1

import sys,os
sys.path.append("/pkg/bin/")
from ztp_helper import ZtpHelpers
from pprint import pprint
import time

ztp_obj=ZtpHelpers()
cmd1 = ztp_obj.xrcmd(cmd)
cmd ={"exec_cmd" : "show install request"}
cmd1 = ztp_obj.xrcmd(cmd)
cmd ={"exec_cmd" : "install add source harddisk:/ ncs5500-6.5.1-SMU-Package-2.tar"}
cmd1 = ztp_obj.xrcmd(cmd)
cmd ={"exec_cmd" : "show install request"}
cmd1 = ztp_obj.xrcmd(cmd)
pprint(cmd1)

