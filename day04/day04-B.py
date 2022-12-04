#!/usr/bin/env python3

# Day 04: A, B

import re
import sys

# Constants

PAIRS_RX = r'(\d+)-(\d+),(\d+)-(\d+)'

# Functions

def read_pairs(stream=sys.stdin):
    return [
        (set(range(As, Ae + 1)), set(range(Bs, Be + 1)))
        for As, Ae, Bs, Be in map(lambda l: map(int, re.findall(PAIRS_RX, l)[0]), stream)
    ]

# Main Execution

def main():
    pairs     = read_pairs()
    contained = sum(
        1 for p1, p2 in pairs if (p1 & p2) in (p1, p2)
    )
    disjoints = sum(
        1 for p1, p2 in pairs if not p1.isdisjoint(p2)
    )
    print(f'Day 4-A: {contained}')
    print(f'Day 4-B: {disjoints}')

if __name__ == '__main__':
    main()
