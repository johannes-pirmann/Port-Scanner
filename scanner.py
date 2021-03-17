from socket import *
import time
starting_time = time.time()
system_ports = (0,1023)
user_ports = (1024, 49151)
#Needed: Address, Ports

"""
Establish a connection through sockets
-> If connection successfull -> Port Open
"""

def testport(ip_address, port_address):
    s = socket(AF_INET, SOCK_STREAM)
    conn = s.connect_ex((ip_address, port_address))
    if conn == 0:
        print(f'Port {port_address} is open.')
    s.close()


if __name__ == '__main__':
    ip_address = input('Enter target IP address: ')
    print(f'Target: {ip_address}')
    choose_ports = input('Enter 1 for ports 0-1023. Enter 2 for ports 1024-49151: ')
    if choose_ports == '1':
        use_ports = system_ports
    elif choose_ports == '2':
        use_ports = user_ports
    else:
        print('wrong input!')

    for i in range(use_ports[0],use_ports[1]):
        testport(ip_address, i)


print(f'It took {time.time()-starting_time}')
