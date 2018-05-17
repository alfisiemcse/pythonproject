import telnetlib
import getpass
import sys
HOST = "192.168.122.4"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
tn.write(b"enable"+ b"\n")
tn.write(b"cisco\n"+b"\n")
#tn.write(b"conf t\n"+b"\n")
#tn.write(b"int loopback 0\n"+b"\n")
#tn.write(b"ip address 1.1.1.1 255.255.255.255\n"+b"\n")
#tn.write(b"no shut"+b"\n")
#tn.write(b"end"+b"\n")
tn.write(b"show run"+b"\n")
#tn.write(b"end"+b"\n")
#tn.write(b"end"+b"\n")
#tn.write(b"end"+b"\n")
tn.write(b"exit"+b"\n")
tn.close()
output =str(tn.read_all())
f = open("alfismacho.txt",'w')
f.write(output)
f.close()

print(tn.read_all().decode('ascii'))
