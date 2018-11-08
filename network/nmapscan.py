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
    nm.scan(hosts=host, arguments='-Pn -sR -sC -sS --osscan-limit')
    print(nm._scan_result)
    return analyze(nm._scan_result)

# data dict of nmap scan result
def analyze(data):
    try:
        print('Scanned: ' + data['nmap']['command_line'])
        print('===================================')
        print('tcp ports:')

        services = {}

        for ip in data['scan']:
            services[ip] = {}
            print('IP Adress: ' + ip)
            services[ip]['os'] = check_os(data['scan'][ip])
            for port in data['scan'][ip]['tcp']:
                print(str(port) + ' ' + data['scan'][ip]['tcp'][port]['state'] + ' ' + data['scan'][ip]['tcp'][port]['name'])
                services[ip][port] = [data['scan'][ip]['tcp'][port]['state'],data['scan'][ip]['tcp'][port]['product'], data['scan'][ip]['tcp'][port]['version']]
        return services
                # services : {
                #   ip : {
                #     port : [state, product, version],
                #     port : [state, product, version],
                #     etc
                #   }
                # }
    except:
        print('Analyzing Nmap data failed.')
        sys.exit()

# Temporary solution for determining the OS of scanned machine
def check_os(data):
    # if 'linux' in data or 'ubuntu' in data:
    if any(x in str(data).lower() for x in ['linux', 'ubuntu', 'debian']):
        return 'linux'
    # elif 'bsd' in data or 'unix' in data:
    elif any(x in str(data).lower() for x in ['bsd', 'unix']):
        return 'unix'
    elif 'windows' in str(data).lower():
        return 'windows'
    # elif 'macosx' in data or 'apple' in data:
    elif any(x in str(data).lower() for x in ['macosx', 'apple', 'osx']):
        return 'osx'
    return ''