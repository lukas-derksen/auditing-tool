import subprocess
import re

def initialize(host):
    scan = subprocess.Popen(['dirb', host, '/tmp/words'], stdout=subprocess.PIPE)
    return analyze(scan.communicate())


def analyze(data):
    data = re.split('\n |\r', data[0].decode('ascii'))
    links = []
    for line in data:
        if (len(line) > 0 and line[0] == '+'):
            links.append(line.split(' ')[1])
    return links