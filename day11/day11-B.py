#!/usr/bin/env python3

from collections import deque
import math
import sys

# Structures

class Monkey:
    def __init__(self, id, items, inspect, check, divider):
        self.id          = id
        self.items       = items
        self.inspect     = inspect
        self.check       = check
        self.divider     = divider
        self.inspections = 0

    @staticmethod
    def parse_monkey(stream=sys.stdin):
        try:
            monkey_id        = int(stream.readline().split()[-1][:-1])
            monkey_items     = deque(map(int, stream.readline().split(':')[-1].split(',')))
            monkey_operation = stream.readline().split('=')[-1]
            monkey_inspect   = lambda old: eval(monkey_operation)
            monkey_divider   = int(stream.readline().strip().split()[3])
            monkey_true      = int(stream.readline().strip().split()[5])
            monkey_false     = int(stream.readline().strip().split()[5])
            monkey_check     = lambda lvl: monkey_false if lvl % monkey_divider else monkey_true
            return Monkey(monkey_id, monkey_items, monkey_inspect, monkey_check, monkey_divider)
        except IndexError:
            return None

    @staticmethod
    def parse_monkeys(stream=sys.stdin):
        while monkey := Monkey.parse_monkey(stream):
            yield monkey
            stream.readline()

    def __str__(self):
        return f'Monkey {self.id}: {", ".join(map(str, self.items))} [{self.inspections}]'

# Functions

def simulate_monkeys(monkeys, rounds=20, divider=3):
    for round in range(1, rounds + 1):
        for monkey in monkeys:
            while monkey.items:
                old_item   = monkey.items.popleft()
                new_item   = monkey.inspect(old_item) % divider
                new_monkey = monkey.check(new_item)
                monkeys[new_monkey].items.append(new_item)

                monkey.inspections += 1

        print(f'Round {round}')
        print_monkeys(monkeys)

def print_monkeys(monkeys):
    for monkey in monkeys:
        print(monkey)
    print()

# Main Execution

def main():
    monkeys = list(Monkey.parse_monkeys())
    divider = math.lcm(*[m.divider for m in monkeys])
    simulate_monkeys(monkeys, 10000, divider)
    sussy_monkeys = sorted(monkeys, key=lambda m: m.inspections)[-2:]
    print(f'Day 11-B: {sussy_monkeys[0].inspections * sussy_monkeys[1].inspections}')

if __name__ == '__main__':
    main()
