from time import sleep
from pprint import pprint
from zapv2 import ZAPv2
import json
from pathlib import Path

with open(Path('../config.json'), 'r') as f:
    config = json.load(f)

key = config['ZAProxy']['key']
zap = ZAPv2(apikey=key)

def initialize(host):
    # zap = ZAPv2(apikey=key)
    try:
        zap.urlopen(host)
        sleep(2)
        spider(host)
        passive_scan()
        active_scan(host)
        return get_alerts()
    except:
        print('WARNING: Make sure Zaproxy is running in Daemon mode with the designated key: {0}'.format(key))

def spider(host):
    scanid = zap.spider.scan(host)
    sleep(2)
    while int(zap.spider.status(scanid)) < 100:
        print('Spider progress %: {}'.format(zap.spider.status(scanid)))
        sleep(2)
    print('Spider completed')
    return scanid

def passive_scan():
    while int(zap.pscan.records_to_scan) > 0:
        print('Records to passive scan: {}'.format(zap.pscan.records_to_scan))
        sleep(2)
    print('Passive scan completed')

def active_scan(host):
    print('Active scanning target {}'.format('host'))
    scanid = zap.ascan.scan(host)
    sleep(2)
    while int(zap.ascan.status(scanid)):
        print('Scan progress %: {}'.format(zap.ascan.status(scanid)))
        sleep(5)
    print('Active scan completed')

def get_alerts():
    print('Hosts: {}'.format(', '.join(zap.core.hosts)))
    print('Alerts: ')
    pprint(zap.core.alerts())
    return zap.core.alerts()