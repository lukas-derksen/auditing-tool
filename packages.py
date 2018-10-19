import subprocess

def install(package):
    subprocess.run(['pip', 'install', package])