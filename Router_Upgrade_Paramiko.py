import paramiko
import time

user = "vika4539"
password = "Sachin@123"

peyto = raw_input('Enter peyto IP: ')

class connection:
    #this is starting connection to router
    def __init__(self, ip):
        self.ip = ip
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname=ip,username=user,password=password,look_for_keys=False, allow_agent=False)
        #self.ssh_client.invoke_shell()
    # for show commands file /input etc we can use
    def show_commands(self,commands):
        router_conn = self.ssh_client.invoke_shell()
        time.sleep(1)
        router_conn.send("ter len 0\n")
        output = router_conn.recv(65535)
        #print(output)
        for command in commands:
            router_conn.send(command)
            time.sleep(2)
        output1 = router_conn.recv(6553500)
        return output1


# taking class name connection in router variable
try:
   router = connection(peyto)
except Exception:
    print('Please check you IP and Enter correct IP or Device is unreachable/Down')
    router = connection(peyto)


arp_vrf = "show arp vrf all | i Dynamic\n"
#router = connection(peyto)
output = router.show_commands(arp_vrf)
print(output)

new2 = output.splitlines()[6:-1]
#print(new2)
evpn_nei_list = []

for i in new2:
    #evpn_nei_list = []
    Z = i.split(' ')
    #print(type(Z))
    evpn_nei_list.append(Z)
#print(evpn_nei_list)

dict1 = {}

for h in evpn_nei_list:
    #print(h)
    if h[-1] not in dict1:
        dict1[h[-1]] = []
    dict1[h[-1]].append(h[0])
#print(dict1)

dict7 = {}
for key1,value1 in dict1.items():
    dict7[key1] = dict7
    dict7[key1] = str(len(value1))
print(dict7)


# Processing EVPN EVI NEI Command
evpn_nei = 'show evpn evi nei\n'
#router = connection(peyto)
output = router.show_commands(evpn_nei)
#print(output)
new1 = output.splitlines()[9:-1]
#print(new1)
evi = []
for i in new1:
    #evpn_nei_list = []
    Z = i.strip().split('MPLS')

    evi.append(Z)
#print(evpn_nei_list)
dict2 = {}
for h in evi:
    #print(h)
    if h[-1] not in dict2:
        dict2[h[-1]] = []
    dict2[h[-1]].append(h[0].strip())
print(dict2)
#login to each EVPN EVI NEI for Command Output
commands1 = open('Peyto_upgrade_pre_post_output.txt','r')

try:
   router = connection(peyto)
except Exception:
   print('Please check you IP and Enter correct IP or Device is unreachable/Down')
   router = connection(peyto)
output4 = router.show_commands(commands1)
file4 = open(peyto + '.txt','a')
file4.write(output4)

for key ,value in dict2.items():
    key1 = key.strip()
    print('For router ' + key1)
    try:
       router = connection(key1)
    except Exception:
       print('Please check you IP and Enter correct IP or Device is unreachable/Down')
       router = connection(key1)
    commands1.seek(0)
    file1 = open(key1 + '.txt','a')
    for line in commands1:
       output = router.show_commands(commands1)
       #time.sleep(3)
       file1.write(output)
    file1.close()

a = ''
for key, value in dict1.items():
    a = a + key + '|'
j = a.strip('|')

nei_arp_cmd = ["show arp vrf all | i " '"'+ j +'"'+ ' | exclude Interface\n' , "show bundle brief\n" ,
               "sh interfaces description | exclude admin-down | include Te0/0\n","sh bundle | include Te0/0\n"]
for key ,value in dict2.items():
    key1 = key.strip()
    print('For router ' + key1)
    try:
       router = connection(key1)
    except Exception:
       print('Please check you IP and Enter correct IP or Device is unreachable/Down')
       router = connection(key1)
    output = router.show_commands(nei_arp_cmd)
    print(output)

try:
   router = connection(peyto)
except Exception:
    print('Please check you IP and Enter correct IP or Device is unreachable/Down')
    router = connection(peyto)

Te_interfaces = 'show run formal | i TenGigE | i "bundle id"\n'
output = router.show_commands(Te_interfaces)
output_int = output.splitlines()[7:-1]
print(output_int)

interface_shutdown = []
for line in output_int:
   interface = line.split( )[1]
   interface_shutdown.append(interface)
print(interface_shutdown)

list1 = ['conf t\n']
for line in interface_shutdown:
    A = "interface " + line + " shutdown\n"
    list1.append(A)
D = ['router isis T4 set-overload-bit\n','root\n','commit\n','exit\n']
for line in D:
   list1.append(line)

print(list1)
