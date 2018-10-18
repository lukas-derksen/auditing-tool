import subprocess

def install():
    subprocess.run(['pip', 'install', 'nmap'])
    subprocess.run(['pip', 'install', 'click'])