#!/usr/bin/env python3

import collections
import sys

# Constants

WINDOW_SIZE = 4

# Functions

def find_first_marker(datastream):
    window = collections.deque(maxlen=4)
    for position, packet in enumerate(datastream, 1):
        window.append(packet)
        if len(window) == len(set(window)) == WINDOW_SIZE:
            return position

# Main Execution

def main():
    for datastream in map(str.strip, sys.stdin):
        print(f'Day 06-A: {find_first_marker(datastream)}')

if __name__ == '__main__':
    main()
