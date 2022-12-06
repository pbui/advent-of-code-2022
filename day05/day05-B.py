#!/usr/bin/env python3

import re
import sys

# Functions

def read_stacks(stream=sys.stdin):
    # Read crates as matrix
    matrix = []
    for line in stream:
        if not line.strip():
            break
        matrix.append(line)

    # Parse matrix into stacks
    stacks = {}
    for c in range(1, len(matrix[0]), 4):
        stack = int(matrix[-1][c])
        stacks[stack] = [matrix[-r][c] for r in range(2, len(matrix) + 1) if matrix[-r][c].strip()]
    return stacks

def parse_moves(stacks, stream=sys.stdin):
    for line in stream:
        n, source, target = map(int, re.match(r'move (\d+) from (\d+) to (\d+)', line).groups())
        stacks[target].extend(stacks[source][-n:])
        stacks[source] = stacks[source][:-n]

# Main Execution

def main():
    stacks = read_stacks()
    parse_moves(stacks)
    tops   = ''.join(d[-1] for s, d in sorted(stacks.items()))
    print(f'Day 05-B: {tops}')

if __name__ == '__main__':
    main()
