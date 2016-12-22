#!/usr/env python
# -*- encoding:utf-8 -*-
"""extract ignore cond from .flake8."""

import sys

INPUT_PATH = './github_flake8.txt'
OUTPUT_PATH = './ignores.txt'


def main(argv):
    """main function."""
    keyword = argv[1]
    output_path = keyword + '.txt'
    with open(INPUT_PATH, 'r') as fi, open(output_path, 'w') as fo:
        for line in fi:
            if line.find(keyword) != -1:
                print line
                fo.write(line)

if __name__ == '__main__':
    main(sys.argv)
