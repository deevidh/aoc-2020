import itertools
import math
from aocd import data


def get_input():
    processed_data = []
    for line in data.splitlines():
        processed_data.append(int(line))
    return processed_data


def calculate_expenses(expenses, n):
    for combi in itertools.combinations(expenses, n):
        if sum(combi) == 2020:
            print("Found product: {}".format(math.prod(combi)))


expenses = get_input()

# Part 1
calculate_expenses(expenses, 2)

# Part 2
calculate_expenses(expenses, 3)
