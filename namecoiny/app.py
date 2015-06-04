'''
namecoiny

Usage:
  namecoiny create digital_ocean -t <token> [-r <region>]
  namecoiny -h | --help
  namecoiny -v | --version

Options:
  -h --help      Show this screen
  -v --version   Show version
'''

import os
import socket
import time

from docopt import docopt
from paramiko.client import SSHClient, AutoAddPolicy
from paramiko.ssh_exception import SSHException

from .vm import DigitalOceanDroplet

BOOTSTRAP_SCRIPT_URL = 'https://raw.githubusercontent.com/maurycyp/namecoiny/master/bootstrap.sh'
CMD = 'curl %s | sh' % BOOTSTRAP_SCRIPT_URL
VM_NAME = 'namecoiny'
PUBLIC_KEY_PATH = os.environ['NAMECOINY_PUBLIC_KEY_PATH']
PRIVATE_KEY_PATH = os.environ['NAMECOINY_PRIVATE_KEY_PATH']
TIMEOUT = 3  # seconds
MAX_CONNECTION_ATTEMPTS = 60


def main():
    args = docopt(__doc__, version='namecoiny 0.1.0')

    token = args['<token>']
    region = args['<region>']

    print 'Creating VM...'
    vm = DigitalOceanDroplet(token)
    vm.create(VM_NAME, PUBLIC_KEY_PATH, PRIVATE_KEY_PATH)

    print 'Connecting...'
    ssh_client = SSHClient()
    ssh_client.load_system_host_keys()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    connect(ssh_client, vm.ip_address, PRIVATE_KEY_PATH)

    print 'Running bootstrap...'
    stdin, stdout, stderr = ssh_client.exec_command(CMD)
    ssh_client.close()

    print 'Backend IP address:', vm.ip_address
    print 'Backend password:'


def connect(ssh_client, ip_address, private_key_path):
    for i in xrange(1, MAX_CONNECTION_ATTEMPTS):
        try:
            ssh_client.connect(ip_address,
                               username='root',
                               key_filename=private_key_path,
                               timeout=TIMEOUT)
            return
        except (socket.error, SSHException) as e:
            time.sleep(5)
        print 'Could not connect to VM'
