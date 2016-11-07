#!/usr/bin/env python
# -*- encoding:utf-8 -*-
"""shrink data to 1-nth lines."""

import random
import sys


def main(argv):
    """main function."""
    input_path = argv[1]
    output_path = argv[2]
    n = int(argv[3])
    header_lines = 3
    with open(input_path, 'r') as fi:
        input_data_lines = len(fi.readlines()) - header_lines
    max_data_lines = int(input_data_lines  / n)
    print "  OUTPUT: " + str(max_data_lines + header_lines) + " lines."

    # create random boolean list, when True the line will be output.
    chosen_list = []
    reserve_list = []
    for i in range(0, input_data_lines):
        rand = int(random.random() * input_data_lines)
        if rand <= max_data_lines:
            chosen_list.append(True)
        else:
            reserve_list.append(i)
            chosen_list.append(False)
    shortage_lines = max_data_lines - (input_data_lines - len(reserve_list))
    if shortage_lines > 0:
        for j in range(0, shortage_lines):
            i = reserve_list.pop(int(random.random() * len(reserve_list)))
            chosen_list[i] = True

    with open(input_path, 'r') as fi, open(output_path, 'w') as fo:
        for i in range(0, header_lines):
            fo.write(fi.readline())
        j = 0
        for i in range(0, len(chosen_list)):
            if chosen_list[i]:
                fo.write(fi.readline())
                j += 1
                if j == max_data_lines:
                    exit()
            else:
                fi.readline()

if __name__=="__main__":
    if len(sys.argv) != 4: 
        print "  USAGE: $ python shrink.py {input} {output} {dominator of devide}"
        exit()
    main(sys.argv)
