#!/usr/bin/env python
# coding=utf-8

"""Punchout v0.1

Usage:
    punchout.py

Options:
    -h --help               Show this screen.
    -v --version            Show version.
"""

from lib.docopt import docopt

def main():
    print "tjo"

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Punchout v0.1')
    main()
    exit()
