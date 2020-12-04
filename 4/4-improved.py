from aocd import data
import re

'''

    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
'''
re_xyr = re.compile('^\d{4}$')
re_hgt = re.compile('^(\d+)(cm|in)$')
re_hcl = re.compile('^#[\da-z]{6}$')
re_ecl = re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$')
re_pid = re.compile('^\d{9}$')


def get_input() -> list:
    list_of_dicts = []
    for document in data.split("\n\n"):
        dict = {}
        for field in re.split(' |\n', document):
            [key, value] = field.split(":")
            dict[key] = value
        list_of_dicts.append(dict)
    return list_of_dicts


def validate_part1(documents: list) -> list:
    valid_documents = []
    for document in documents:
        if len(document) == 8:
            valid_documents.append(document)
        if len(document) == 7 and "cid" not in document.keys():
            valid_documents.append(document)
    return valid_documents


def validate_part2(documents: list) -> list:
    valid_documents = []
    for document in documents:
        if not (re_xyr.match(document['byr']) and 1920 <= int(document['byr']) <= 2002):
            continue
        if not (re_xyr.match(document['iyr']) and 2010 <= int(document['iyr']) <= 2020):
            continue
        if not (re_xyr.match(document['eyr']) and 2020 <= int(document['eyr']) <= 2030):
            continue
        hgt_matches = re_hgt.match(document['hgt'])
        if not hgt_matches:
            continue
        height = hgt_matches[1]
        height_units = hgt_matches[2]
        if height_units == "cm":
            if not (150 <= int(height) <= 193):
                continue
        if height_units == "in":
            if not (59 <= int(height) <= 76):
                continue
        if not (re_hcl.match(document['hcl'])):
            continue
        if not (re_ecl.match(document['ecl'])):
            continue
        if not (re_pid.match(document['pid'])):
            continue
        valid_documents.append(document)
    return valid_documents


documents = get_input()

# Part 1
valid1 = validate_part1(documents)
print("Part 1: {} valid passports".format(len(valid1)))

# Part 2
valid2 = validate_part2(valid1)
print("Part 2: {} valid passports".format(len(valid2)))
