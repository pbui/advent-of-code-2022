#!/usr/bin/env python3

import collections
import os
import sys

# Constants

THRESHOLD = 100000

# Classes

def parse_filesystem(stream=sys.stdin):
    fs  = collections.defaultdict(list)
    cwd = ''

    for line in stream:
        tokens = line.strip().split()

        if tokens[0] == '$' and tokens[1] == 'cd':
            cwd = os.path.abspath(os.path.join(cwd, tokens[2]))
        elif tokens[0] == '$' and tokens[1] == 'ls':
            pass
        elif tokens[0] == 'dir':
            fs[cwd].append(('D', tokens[1], 0))
        else:
            fs[cwd].append(('F', tokens[1], int(tokens[0])))

    return fs

def count_filesystem(fs):
    return count_filesystem_r(fs, '/', collections.defaultdict(int))

def count_filesystem_r(fs, cwd, counts):
    for ftype, fname, fsize in fs[cwd]:
        if ftype == 'F':
            counts[cwd] += fsize
        else:
            path = os.path.abspath(os.path.join(cwd, fname))
            count_filesystem_r(fs, path, counts)
            counts[cwd] += counts[path]
    return counts

# Main Execution

def main():
    fs    = parse_filesystem()
    sizes = count_filesystem(fs)
    print(f'Day 07-A: {sum(size for size in sizes.values() if size <= THRESHOLD)}')

if __name__ == '__main__':
    main()
