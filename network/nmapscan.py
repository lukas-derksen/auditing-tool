import packages
import json
import sys

try:
    import nmap
except (ModuleNotFoundError,ImportError,ImportWarning):
    packages.install("nmap")
    import nmap

def initiate(host):
    print('Scanning host ' + host)
    nm = nmap.PortScanner()
    nm.scan(hosts=host, arguments='-Pn -sR -sC -T4 --osscan-guess --fuzzy')
    analyze(nm._scan_result)


def analyze(data):
    try:
        print('Scanned: ' + data['nmap']['command_line'])
        print('===================================')
        print('tcp ports:')

        services = {}

        for ip in data['scan']:
            services[ip] = {}
            print('IP Adress: ' + ip)
            for port in data['scan'][ip]['tcp']:
                print(str(port) + ' ' + data['scan'][ip]['tcp'][port]['state'] + ' ' + data['scan'][ip]['tcp'][port]['name'])
                services[ip][port] = [data['scan'][ip]['tcp'][port]['state'],data['scan'][ip]['tcp'][port]['product'], data['scan'][ip]['tcp'][port]['version']]
                

    except:
        print('Analyzing Nmap data failed.')