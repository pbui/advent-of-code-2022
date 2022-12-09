#!/usr/bin/env python3

import itertools
import sys

# Constants

BORDER      = -1
DIRECTIONS  = (
    (-1,  0),   # Up
    ( 1,  0),   # Down
    ( 0, -1),   # Left
    ( 0,  1),   # Right
)

# Functions

def read_grid(stream=sys.stdin):
    grid = []
    for line in stream:
        grid.append([BORDER] + list(map(int, line.strip())) + [BORDER])

    grid.insert(0, [BORDER]*len(grid[0]))
    grid.append([BORDER]*len(grid[0]))
    return grid

def is_visible_one(grid, r, c, height, dr, dc):
    # Base case: hit border
    if grid[r][c] == BORDER:
        return True

    # Base case: hit taller tree
    if grid[r][c] >= height:
        return False

    # Recursive: keep going
    return is_visible_one(grid, r + dr, c + dc, height, dr, dc)

def is_visible_any(grid, r, c):
    return any(
        is_visible_one(grid, r + dr, c + dc, grid[r][c], dr, dc) for dr, dc in DIRECTIONS
    )

# Main Execution

def main():
    grid  = read_grid()
    cells = itertools.product(range(1, len(grid) - 1), range(1, len(grid[0]) - 1))
    count = sum(1 for r, c in cells if is_visible_any(grid, r, c))
    print(f'Day 08-A: {count}')

if __name__ == '__main__':
    main()
