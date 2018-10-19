import packages
try:
    import nmap
except (ModuleNotFoundError,ImportError,ImportWarning):
    packages.install("nmap")
    import nmap

def initiate(host):
    print('Scanning host ' + host)
    nm = nmap.PortScanner()
    nm.scan(hosts=host, arguments='-Pn -sR -sC -T4')
    print(nm._scan_result)