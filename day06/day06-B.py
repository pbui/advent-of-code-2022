#!/usr/bin/env python3

import collections
import sys

# Functions

def find_first_marker(datastream, window_size):
    window = collections.deque(maxlen=window_size)
    for position, packet in enumerate(datastream, 1):
        window.append(packet)
        if len(window) == len(set(window)) == window_size:
            return position

# Main Execution

def main():
    for datastream in map(str.strip, sys.stdin):
        print(f'Day 06-A: {find_first_marker(datastream, 4)}')
        print(f'Day 06-B: {find_first_marker(datastream, 14)}')

if __name__ == '__main__':
    main()
