import packages
try:
    import click
except (ModuleNotFoundError,ImportError,ImportWarning):
    packages.install("click")
    import click

from network import nmapscan

@click.group()
def main():
    pass

@main.command()
@click.option('-h', '--host')
def network(host):
    print("Start network scanning")
    nmapscan.initiate(host)

@main.command()
def webapp():
    print("Webapp scanning not yet implemented")

if __name__ == "__main__":
    main()