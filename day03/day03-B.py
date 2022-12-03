#!/usr/bin/env python3

# Day 03: A

import sys

# Functions

def read_groups(stream=sys.stdin):
    lines = list(map(str.strip, stream.readlines()))
    return [
        lines[i:i+3] for i in range(0, len(lines), 3)
    ]

def find_common(groups):
    return [
        (set(c1) & set(c2) & set(c3)).pop() for c1, c2, c3 in groups
    ]

def compute_priority(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

# Main Execution

def main():
    groups     = read_groups()
    commons    = find_common(groups)
    priorities = [compute_priority(item) for item in commons]
    print(f'Day 03-B: {sum(priorities)}')

if __name__ == '__main__':
    main()
