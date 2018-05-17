import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")
tn.write(b"enable"+ b"\n")
tn.write(b"cisco\n"+b"\n")
tn.write(b"conf t\n"+b"\n")
tn.write(b"int loopback 0\n"+b"\n")
tn.write(b"ip address 1.1.1.1 255.255.255.255\n"+b"\n")
tn.write(b"no shut"+b"\n")
tn.write(b"end"+b"\n")
tn.write(b"exit"+b"\n")


print(tn.read_all().decode('ascii'))
