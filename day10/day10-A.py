#!/usr/bin/env python3

from collections import deque
import sys

# Constants

CYCLES = (20, 60, 100, 140, 180, 220)

# Classes

class Machine:
    def __init__(self):
        self.x     = 1
        self.cycle = 1
        self.trace = {}

    def process_instructions(self, stream=sys.stdin):
        for instruction in map(str.strip, stream):
            self.trace[self.cycle] = self.x
            
            if instruction == 'noop':
                self.cycle += 1
            else:
                _, operand = instruction.split()
                self.trace[self.cycle + 1] = self.x
                self.x     += int(operand)
                self.cycle += 2

# Main Execution

def main():
    machine = Machine()
    machine.process_instructions()
    signal_strengths = sum(cycle * machine.trace[cycle] for cycle in CYCLES)

    print(f'Day 10-A: {signal_strengths}')

if __name__ == '__main__':
    main()
