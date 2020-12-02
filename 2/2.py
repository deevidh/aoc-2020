from aocd import data
import re


def get_input():
    processed_data = []
    for line in data.splitlines():
        processed_data.append(line)
    return processed_data


def parse_passwords(passwords):
    pp = []
    for password in passwords:
        match = re.match('^(\d+)-(\d+) ([a-z]): ([a-z]+)', password)
        pp.append([match[1], match[2], match[3], match[4]])
    return pp


def validate_passwords(pp):
    valid_passwords = []
    for p in pp:
        if int(p[0]) <= p[3].count(p[2]) <= int(p[1]):
            valid_passwords.append(p[3])
    return valid_passwords


def validate_passwords2(pp):
    valid_passwords = []
    for p in pp:
        count = 0
        if p[3][int(p[0])-1] == p[2]:
            count += 1
        if p[3][int(p[1])-1] == p[2]:
            count += 1
        if count == 1:
            valid_passwords.append(p[3])
    return valid_passwords


passwords = get_input()
pp = parse_passwords(passwords)

# Part 1
valid = validate_passwords(pp)
print("Part 1 - found {} valid passwords".format(len(valid)))

# Part 2
valid2 = validate_passwords2(pp)
print("Part 2 - found {} valid passwords".format(len(valid2)))
