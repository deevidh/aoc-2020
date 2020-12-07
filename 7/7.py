from aocd import data
import re

parent_re = re.compile('(\w+ \w+) bag')
child_re = re.compile('.*(\d+) (\w+ \w+) bag')

test_data = '''shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.'''


def get_test_input():
    return [rule for rule in test_data.split("\n")]


def get_input():
    return [rule for rule in data.split("\n")]


def build_rule_dict(rawrules: list) -> dict:
    rule_dict = {}
    for rawrule in rawrules:
        parts = rawrule.split("contain")
        parent = parent_re.match(parts[0])[1]
        naughty_children = parts[1].split(",")
        bag_dict = {}
        for naughty_child in naughty_children:
            if "no other" in naughty_child:
                bag_dict = "none"
                continue
            bag_dict[child_re.match(naughty_child)[2]] = child_re.match(naughty_child)[1]
        rule_dict[parent] = bag_dict
    return rule_dict


def one_level_search(rule_dict: dict, name: str) -> list:
    return [item for item in rule_dict if rule_dict[item] != "none"
            and name in rule_dict[item].keys()]


def search_dict(rule_dict: dict, name: str) -> list:
    final_list = []
    one_level = one_level_search(rule_dict, name)
    final_list.extend(one_level)
    while len(one_level) > 0:
        next_level = []
        for new_bag in one_level:
            next_level.extend(one_level_search(rule_dict, new_bag))
        one_level = next_level
        final_list.extend(one_level)
    return list(set(final_list))


# Returns count inclusive of the specified bag, so you may need to subtract 1
def count_children(rule_dict: dict, name: str) -> int:
    if rule_dict[name] == "none":
        return 1
    return (1 + sum(int(rule_dict[name][child])*count_children(rule_dict, child)
            for child in rule_dict[name]))


rawrules = get_input()
rule_dict = build_rule_dict(rawrules)

# Part 1
bag_list = search_dict(rule_dict, "shiny gold")
print("Part 1: {}".format(len(bag_list)))

# Part 2
total_bags = count_children(rule_dict, "shiny gold")
print("Part 2: {}".format(total_bags - 1))
