#!/usr/bin/env python3

# Day 01: A

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
    calories = read_calories()
    print(f'Day 01-A: {max(calories)}')

if __name__ == '__main__':
    main()
