import subprocess

def install(package):
    try:
        subprocess.run(['pip3', 'install', package])
    except:
        print("Failed to install package %s. Try installing it manually instead", package)