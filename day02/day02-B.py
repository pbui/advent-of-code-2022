#!/usr/bin/env python3

# Day 02: A

import sys

# Constants

CHOICES = {
    ('A', 'X'): 'Z',
    ('A', 'Y'): 'X',
    ('A', 'Z'): 'Y',
    
    ('B', 'X'): 'X',
    ('B', 'Y'): 'Y',
    ('B', 'Z'): 'Z',
    
    ('C', 'X'): 'Y',
    ('C', 'Y'): 'Z',
    ('C', 'Z'): 'X',
}

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

def compute_scoreA(first, second):
    return OUTCOMES[(first, second)] + SHAPES[second]

def compute_scoreB(first, second):
    choice = CHOICES[(first, second)]
    return OUTCOMES[(first, choice)] + SHAPES[choice]

# Main Execution

def main():
    rounds  = [line.split() for line in sys.stdin]
    scoresA = [compute_scoreA(*r) for r in rounds]
    scoresB = [compute_scoreB(*r) for r in rounds]

    print(f'Day 01-A: {sum(scoresA)}')
    print(f'Day 01-B: {sum(scoresB)}')

if __name__ == '__main__':
    main()
