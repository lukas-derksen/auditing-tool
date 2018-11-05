import packages
from network import msfrpc
import time

# Object for the msfrpc client
client = None

def initiate(data):
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
    
    for target in data:
        find_exploits(data[target], target)

# data: dict of nmap scan results from current target
# target: ip address of the current target
def find_exploits(data, target):
    print('Starting exploit on ' + target)
    console = client.create_console()
    # Get the console id
    con_id = int(str(console[b'id']).strip()[2:-1])
    print('Console ID: ' + str(con_id))
    client.read_console(con_id)
    # print(client.run_module())
    for port in data:
        if data[port][0] == 'closed' or data[port][1] == '':
            continue
        service = data[port][1]
        version = data[port][2]

        print('Searching exploits for ' + service + ' ' + version)
        client.read_console(con_id)
        search = "search {0} {1}".format(service, version)
        client.write_console(con_id, search)

        # Sleep 1 second for Metasploit to load relevant exploits
        time.sleep(1)
        res = client.read_console(con_id)
        print(res)

    for i in range(0,con_id):
        client.destroy_console(i)

# target: ip address of current target
# port: port for current exploit
# exploit: data dict of current exploit
def exploit(target, port, exploit):
    pass