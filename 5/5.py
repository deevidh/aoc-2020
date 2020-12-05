from aocd import data


def get_input():
    return [line for line in data.split("\n")]


def get_seat_id(seatcode: str) -> int:
    rmin, rmax = 0, 127
    for char in seatcode[0:7]:
        if char == 'F':
            rmax = rmax - ((rmax-rmin+1)/2)
        else:
            rmin = rmin + ((rmax-rmin+1)/2)
    cmin, cmax = 0, 7
    for char in seatcode[7:10]:
        if char == 'L':
            cmax = cmax - ((cmax-cmin+1)/2)
        else:
            cmin = cmin + ((cmax-cmin+1)/2)
    return int((8*rmax) + cmax)


def find_empty_seats(manifest: list) -> list:
    empty_seats = []
    for i in range(0, max(manifest)):
        if i not in manifest:
            if i-1 in manifest and i+1 in manifest:
                empty_seats.append(i)
    return empty_seats


# boarding_passes = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
boarding_passes = get_input()

# Part 1
manifest = [get_seat_id(b_pass) for b_pass in boarding_passes]
print("Part 1: {}".format(max(manifest)))

# Part 2
print("Part 2: {}".format(find_empty_seats(manifest)[0]))
