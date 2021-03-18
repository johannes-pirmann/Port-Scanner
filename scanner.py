from socket import *
import time
import sys
from threading import Thread, Event


starting_time = time.time()
system_ports = (0,1023)
user_ports = (1024, 49151)


def testport(ip_address, port_address, open_ports):
    s = socket(AF_INET, SOCK_STREAM)
    conn = s.connect_ex((ip_address, port_address))
    if conn == 0:
        open_ports.append(port_address)
        #print(f'Port {port_address} is open.')
    s.close()
    return open_ports



def progress(count, total, status=''):
    """
    Progressbar by: vladignatyev
    Source: https://gist.github.com/vladignatyev/06860ec2040cb497f0f3
    """
    bar_len = 50
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total),1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()



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

    open_ports = []
    for i in range(use_ports[0],use_ports[1]):
        
        testport(ip_address, i, open_ports)
        progress(i, use_ports[1], 'Scanning Ports')
    print(f'\nOpen Ports: {open_ports}')

print(f'It took {time.time()-starting_time}')
