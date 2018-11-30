import sys
import os
import packages
try:
    import click
except (ModuleNotFoundError,ImportError,ImportWarning):
    packages.install("click")
    import click

from network import nmapscan, msf
from webapp import dirb, whatweb, zaproxy, bruteforce

@click.group()
def main():
    pass

@main.command()
@click.option('-h', '--host')
def network(host):
    print("Start network scanning")
    data = nmapscan.initiate(host)
    if data is None:
        print('Nmap scan returned no open ports.')
        sys.exit()
    host = click.prompt('What IP should the exploit connect to? (Your public or local IP, depending on whether the target is in your local network or not)')
    msf.initiate(data,host)

@main.command()
@click.option('-h', '--host')
def webapp(host):
    if not 'http' in host:
        print('Invalid URL format: {0}'.format(host))
        print('Use \'http://target\' or \'https://target\'')
        sys.exit()
    print("Started webapp scanning")
    whatweb.initiate(host)
    links = dirb.initialize(host)
    zaproxy.initialize(host)
    for link in links:
        if bruteforce.check_login_form(links):
            print(link)

if __name__ == "__main__":
    main()