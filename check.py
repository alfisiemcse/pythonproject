from __future__ import print_function
from netmiko import ConnectHandler

import sys
import time
import select
import paramiko
import re
fd = open(r'alfisnew.txt','w')
old_stdout = sys.stdout
sys.stdout = fd
host = '192.168.122.4'
platform = 'cisco_ios'
username = 'alfis'
password = 'cisco'
device = ConnectHandler(device_type=platform, ip=host, username=username, password=password)
output = device.send_command('terminal length 0')
output = device.send_command('enable')
output = device.send_command('cisco')
print('##############################################################\n')
print('...................CISCO COMMAND SHOW RUN OUTPUT......................\n')
output = device.send_command('sh run')
print(output)
print('##############################################################\n')
print('...................CISCO COMMAND SHOW IP INT BR OUTPUT......................\n')
output = device.send_command('sh ip int br')
print(output) 
print('##############################################################\n')

fd.close()
