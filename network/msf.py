import packages
from network import msfrpc

# Object for the msfrpc client
c = None

def initiate():
    print('Initiating msfrpc session')
    ip = "127.0.0.1"
    user = "msf"
    passwd = "ZybQZ9je"
    try:
        c = msfrpc.Client(ip,user,passwd)
    except:
        print('msfrpc session failed. Did you set the password correctly?')

def exploit(data, target):
    pass