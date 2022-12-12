#!/usr/bin/env python3

import collections
import heapq
import itertools
import sys

# Constants

DIRECTIONS = (
    (-1,  0),   # Up
    ( 1,  0),   # Down
    ( 0, -1),   # Left
    ( 0,  1),   # Right
)

# Functions

def read_grid(stream=sys.stdin):
    grid = ['Z' + line.strip() + 'Z' for line in stream]
    grid.insert(0, 'Z'*len(grid[0]))
    grid.append('Z'*len(grid[0]))
    return grid

def build_graph(grid):
    graph  = collections.defaultdict(set)
    rows   = list(range(1, len(grid) - 1))
    cols   = list(range(1, len(grid[0]) - 1))
    starts = []
    end    = None

    for r, c in itertools.product(rows, cols):
        v = (r - 1)*len(cols) + (c - 1)
        h = grid[r][c]

        if h in ('S', 'a'): starts.append(v)
        if h == 'E': end = v

        for dr, dc in DIRECTIONS:
            n_r = r + dr
            n_c = c + dc
            n_v = (n_r - 1) * len(cols) + (n_c - 1)
            n_h = grid[n_r][n_c]

            if n_h == 'Z':
                continue

            if n_h == 'E' and h != 'z':
                continue

            if h == 'S' or abs(ord(h) - ord(n_h)) <= 1 or ord(h) > ord(n_h):
                graph[v].add(n_v)

    return graph, starts, end

def walk_graph(graph, start, end):
    frontier = [(0, start)]
    visited  = set()

    while frontier:
        distance, vertex = heapq.heappop(frontier)

        if vertex in visited:
            continue

        if vertex == end:
            return distance

        visited.add(vertex)

        for neighbor in graph[vertex]:
            heapq.heappush(frontier, (distance + 1, neighbor))

    return sys.maxsize

# Main Execution

def main():
    grid               = read_grid()
    graph, starts, end = build_graph(grid)
    steps              = min(walk_graph(graph, start, end) for start in starts)

    print(f'Day 12-B: {steps}')

if __name__ == '__main__':
    main()
