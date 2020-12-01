import itertools
import math


def get_input():
    processed_data = []
    raw_data = open("1/input.txt", "r")
    for line in raw_data:
        processed_data.append(int(line.strip('\n')))
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
