import sys
import packages
try:
    import click
except (ModuleNotFoundError,ImportError,ImportWarning):
    packages.install("click")
    import click

from network import nmapscan, msf

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
    msf.initiate(data)

@main.command()
def webapp():
    print("Webapp scanning not yet implemented")

if __name__ == "__main__":
    main()