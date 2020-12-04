from aocd import data
import re
import numpy

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


# I had to use the test data for debugging my code
def get_test_input():
    raw_data = open("4/test_data", "r")
    rawdata = raw_data.read()
    return [line for line in rawdata.read().split("\n\n")]


def get_input():
    return [line for line in data.split("\n\n")]


def validate(fields):
    tf = 0
    val_data = {}
    for field in fields:
        if field == '':
            continue
        [header, data] = field.split(":")
        if header == 'byr':
            if re_xyr.match(data):
                idata = int(data)
                if 1920 <= idata <= 2002:
                    val_data[header] = True
                    tf += 1
                else:
                    val_data[header] = False
        if header == 'iyr':
            if re_xyr.match(data):
                if 2010 <= int(data) <= 2020:
                    val_data[header] = True
                    tf += 1
                else:
                    val_data[header] = False
        if header == 'eyr':
            if re_xyr.match(data):
                if 2020 <= int(data) <= 2030:
                    val_data[header] = True
                    tf += 1
                else:
                    val_data[header] = False
        if header == 'hgt':
            if re_hgt.match(data):
                hgt_matches = re_hgt.match(data)
                if hgt_matches[2] == "cm":
                    if 150 <= int(hgt_matches[1]) <= 193:
                        tf += 1
                        val_data[header] = True
                    else:
                        val_data[header] = False
                if hgt_matches[2] == "in":
                    if 59 <= int(hgt_matches[1]) <= 76:
                        tf += 1
                        val_data[header] = True
                    else:
                        val_data[header] = False
        if header == 'hcl':
            if re_hcl.match(data):
                tf += 1
                val_data[header] = True
            else:
                val_data[header] = False
        if header == 'ecl':
            if re_ecl.match(data):
                tf += 1
                val_data[header] = True
            else:
                val_data[header] = False
        if header == 'pid':
            if re_pid.match(data):
                tf += 1
                val_data[header] = True
            else:
                val_data[header] = False
    type(val_data)
    return tf == 7


def simple_fields(documents, validate_flag):
    count = 0
    for document in documents:
        fields = re.split(' |\n', document)
        if len(fields) == 8:
            if validate_flag:
                if validate(fields):
                    count += 1
            else:
                count += 1
        elif len(fields) == 7:
            def func(x): return re.match('cid:', x)
            cid_map = list(map(func, fields))
            if not numpy.any(cid_map):
                if validate_flag:
                    if validate(fields):
                        count += 1
                else:
                    count += 1
    return count


documents = get_input()

# Part 1
valid1 = simple_fields(documents, False)
print("Part 1: {}".format(valid1))

# Part 2
valid2 = simple_fields(documents, True)
print("Part 2: {}".format(valid2))
