#!/usr/bin/env python3

# Day 02: A

import sys

# Constants

OUTCOMES = {
    ('A', 'X'): 3,
    ('A', 'Y'): 6,
    ('A', 'Z'): 0,
    
    ('B', 'X'): 0,
    ('B', 'Y'): 3,
    ('B', 'Z'): 6,
    
    ('C', 'X'): 6,
    ('C', 'Y'): 0,
    ('C', 'Z'): 3,
}

SHAPES = {
    'A': 1, # Rock
    'B': 2, # Paper
    'C': 3, # Scissor

    'X': 1, # Rock
    'Y': 2, # Paper
    'Z': 3, # Scissor
}

# Functions

def compute_score(first, second):
    return OUTCOMES[(first, second)] + SHAPES[second]

def read_rounds(stream=sys.stdin):
    return [compute_score(*line.split()) for line in stream]

# Main Execution

def main():
    rounds = read_rounds()
    print(f'Day 01-A: {sum(rounds)}')

if __name__ == '__main__':
    main()
