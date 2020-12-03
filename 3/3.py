from aocd import data


def get_input():
    processed_data = []
    for line in data.splitlines():
        processed_data.append(line)
    return processed_data


def traverse(forest, path):
    trees = 0
    xcoord = 0
    ycoord = 0
    xmax = len(forest[0])
    while ycoord < len(forest):
        if forest[ycoord][xcoord] == "#":
            trees += 1
        xcoord = (xcoord + path[0]) % xmax
        ycoord = ycoord + path[1]
    return trees


forest = get_input()

# Part 1
trees1 = traverse(forest, [3, 1])
print("Part 1: {} trees".format(trees1))

# Part 2
total = 1
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
for slope in slopes:
    total *= traverse(forest, slope)
print("Part 2: {} trees".format(total))
