#!/usr/bin/env python3

# Day 03: A

import sys

# Functions

def read_rucksacks(stream=sys.stdin):
    return [
        (line[:len(line)//2], line[len(line)//2:]) for line in map(str.strip, stream)
    ]

def find_common(rucksacks):
    return [
        (set(c1) & set(c2)).pop() for c1, c2 in rucksacks
    ]

def compute_priority(item):
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

# Main Execution

def main():
    rucksacks  = read_rucksacks()
    commons    = find_common(rucksacks)
    priorities = [compute_priority(item) for item in commons]
    print(f'Day 03-A: {sum(priorities)}')

if __name__ == '__main__':
    main()
