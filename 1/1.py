def get_input():
    processed_data = []
    raw_data = open("1/input.txt", "r")
    for line in raw_data:
        processed_data.append(int(line.strip('\n')))
    return processed_data


def calculate_expenses(expenses):
    for x in expenses:
        for y in expenses:
            total = x + y
            if total == 2020:
                print("{} * {} = {}".format(x, y, x*y))


def calculate_expenses_3(expenses):
    for x in expenses:
        for y in expenses:
            for z in expenses:
                total = x + y + z
                if total == 2020:
                    print("{} * {} * {} = {}".format(x, y, z, x*y*z))


expenses = get_input()

# Part 1
calculate_expenses(expenses)

# Part 2
calculate_expenses_3(expenses)
