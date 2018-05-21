#import jason
from napalm import get_network_driver
from sys import exit

host_ip = input("Please enter your host device's IP : ")
user_name = input ("Please enter your host device's USERNAME : ")
pass_word = input("Please enter your PASSWORD : ")
secret_pass = input("Please enter your enable PASSWORD : ")

driver = get_network_driver('ios')
optional_argument = {'secret' : secret_pass}
r3 = driver(hostname=host_ip,username=user_name,password=pass_word,optional_args=optional_argument)

r3.open()

def general_facts():
	ios_output = r3.get_facts()
	f = open ("test1.txt",'w')
	for i,j in ios_output.items():
		f.write(str(i)+" : "+str(j)+"\n")
	f.close()

def interface_info():
	ios_output = r3.get_interfaces()
	f = open("test2.txt",'w')
	for i,j in ios_output.items():
		f.write(str(i)+" : "+str(j)+"\n")
	f.close()

def mac_address_table():
	ios_output = r3.get_mac_address_table()
	f = open ("test3.txt",'w')
	for i,j in ios_output.items():
		f.write(str(i)+" : "+str(j)+"\n")
	f.close()

def arp_table():
	ios_output = r3.get_arp_table()
	f = open ("test4.txt",'w')
	for i,j in ios_output.items():
		f.write(str(i)+" : "+str(j)+"\n")
	f.close()

def lldp_neighbors():
	ios_output = r3.get_lldp_neighbors()
	f = open ("test5.txt",'w')
	for i,j in ios_output.items():
		f.write(str(i)+" : "+str(j)+"\n")
	f.close()

def enivonment():
	ios_output = r3.get_environment()
	f = open ("test6.txt",'w')
	for i,j in ios_output.items():
		f.write(str(i)+" : "+str(j)+"\n")
	f.close()

def firewallpolicies():
	ios_output = r3.get_firewall_policies()
	f = open ("test7.txt",'w')
	for i,j in ios_output.items():
		f.write(str(i)+" : "+str(j)+"\n")
	f.close()

def interface_ip():
	ios_output = r3.get_interfaces_ip()
	f = open ("test8.txt",'w')
	for i,j in ios_output.items():
		f.write(str(i)+" : "+str(j)+"\n")
	f.close()

def ipv6neighbour():
	ios_output = r3.get_ipv6_neighbors_table()
	f = open ("test9.txt",'w')
	for i,j in ios_output.items():
		f.write(str(i)+" : "+str(j)+"\n")
	f.close()

def snmpinformation():
	ios_output = r3.get_snmp_information()
	f = open ("test10.txt",'w')
	for i,j in ios_output.items():
		f.write(str(i)+" : "+str(j)+"\n")
	f.close()

def users():
	ios_output = r3.get_users()
	f = open ("test4.txt",'w')
	for i,j in ios_output.items():
		f.write(str(i)+" : "+str(j)+"\n")
	f.close()

users()
snmpinformation()
ipv6neighbour()
interface_ip()
firewallpolicies()
enivonment()
lldp_neighbors()
arp_table()
mac_address_table()
general_facts()