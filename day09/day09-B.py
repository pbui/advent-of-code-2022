#!/usr/bin/env python3

from dataclasses import dataclass, astuple

import math
import sys

# Constants

DIRECTIONS = (
    (-1, -1),
    (-1,  0),
    (-1,  1),
    ( 0, -1),
    ( 0,  1),
    ( 1, -1),
    ( 1,  0),
    ( 1,  1),
)

# Structures

@dataclass
class Point:
    x: int = 0
    y: int = 0

# Functions

def is_adjacent(p1, p2):
    if p1.x == p2.x or p1.y == p2.y:
        return math.hypot(p1.x - p2.x, p1.y - p2.y) <= 1.0
    else:
        return math.hypot(p1.x - p2.x, p1.y - p2.y) <= math.hypot(1, 1)

def read_moves(stream=sys.stdin):
    for line in stream:
        direction, magnitude = line.split()
        yield direction, int(magnitude)

def process_moves(moves, n=2):
    points  = [Point() for _ in range(n)]
    visited = set([astuple(points[-1])])

    for direction, magnitude in moves:
        for _ in range(magnitude):
            if   direction == 'R': points[0].x += 1
            elif direction == 'L': points[0].x -= 1
            elif direction == 'U': points[0].y += 1
            elif direction == 'D': points[0].y -= 1

            for i in range(1, len(points)):
                head = points[i - 1]
                tail = points[i]

                if not is_adjacent(head, tail):
                    points[i] = update_tail(tail, head)
                    
            visited.add(astuple(points[-1]))
            
    return visited

def update_tail(tail, head):
    points = (Point(tail.x + dx, tail.y + dy) for dx, dy, in DIRECTIONS)
    moves  = ((math.hypot(p.x - head.x, p.y - head.y), p) for p in points)
    return sorted(moves, key=lambda m: m[0])[0][1]

# Main Execution

def main():
    moves     = list(read_moves())
    visited2  = process_moves(moves, 2)
    visited10 = process_moves(moves, 10)
    print(f'Day09-A: {len(visited2)}')
    print(f'Day09-B: {len(visited10)}')

if __name__ == '__main__':
    main()
