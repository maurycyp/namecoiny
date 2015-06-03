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

from docopt import docopt

def main():
    args = docopt(__doc__, version='namecoiny 0.1.0')

    token = args['token']
