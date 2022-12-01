#!/usr/bin/env python3

# Day 01: B

import sys

# Functions

def read_calories():
    calories = []
    current  = []
    for line in sys.stdin:
        if line.strip():
            current.append(int(line))
        else:
            calories.append(sum(current))
            current = []
    calories.append(sum(current))
    return calories

# Main Execution

def main():
    calories = sorted(read_calories(), reverse=True)
    print(f'Day 01-A: {max(calories)}')
    print(f'Day 01-B: {sum(calories[:3])}')

if __name__ == '__main__':
    main()
