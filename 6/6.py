from aocd import data
from collections import Counter


def get_input():
    return [group.split("\n") for group in data.split("\n\n")]


def get_unique_answers(group: list) -> list:
    unique_answers = set("".join(group))
    return list(unique_answers)


def get_everyone_answers(group: list) -> list:
    distribution = Counter("".join(group))
    return [answer for answer, count in distribution.items() if count == len(group)]


groups = get_input()

# Part 1
total = sum([len(get_unique_answers(group)) for group in groups])
print("Part 1: {}".format(total))

# Part 2
total = sum([len(get_everyone_answers(group)) for group in groups])
print("Part 2: {}".format(total))
