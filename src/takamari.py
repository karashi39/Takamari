#!/usr/bin/env python
#! -*- encoding:utf-8 -*-
"""nemui."""

import sys

sys.path.append('./src')
from hello import HelloWorld


def main(argv):
    """majide nemui."""
    hello = HelloWorld()
    print hello.say_hello(argv[1])

if __name__ == '__main__':
    main(sys.argv)
