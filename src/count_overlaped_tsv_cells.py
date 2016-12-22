#!/user/env python
# -*- encoding: utf-8 -*-
"""load tsv and count overlaped keys."""

import csv
import sys


def main(argv):
    """main function."""
    input_path = argv[1]
    key_length = int(argv[2])

    # list up overlaped keys.
    with open(input_path, 'r') as f:
        reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_ALL)
        next(reader)  # skip header
        keys = {}  # {unique keys: count overlaped times}.
        for line in reader:
            key = keyset_to_str(line[:key_length])
            if key in keys.keys():
                keys[key] += 1
                continue
            keys.update({key: 0})

    # display result.
    if sum(keys.values()) == 0:
        print '[RESULT] there is no overlapped key.'
        return
    print '[RESULT] overlaped keys below.'
    for key, value in keys.items():
        if value > 0:
            # value count is 1 when there is 2 same keys, so value + 1.
            print 'the key "' + key + '" appears ' + str(value + 1) + 'times.'

    return


def keyset_to_str(keyset):
    """convert multiple keyset into single str key."""
    str_key = ''
    for i in xrange(len(keyset)):
        str_key += keyset[i] + ' '
    return str_key

if __name__ == '__main__':
    main(sys.argv)
