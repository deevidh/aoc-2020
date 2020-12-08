from aocd import data

test_data = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''


def get_test_input():
    return [[ins for ins in line.split(" ")] for line in test_data.split("\n")]


def get_input():
    return [[ins for ins in line.split(" ")] for line in data.split("\n")]


def execute(instructions: list, exec: int, acc: int) -> (int, int):
    if instructions[exec][0] == "acc":
        return exec + 1, acc + int(instructions[exec][1])
    if instructions[exec][0] == "jmp":
        return exec + int(instructions[exec][1]), acc
    if instructions[exec][0] == "nop":
        return exec + 1, acc


def run_code(code: list, exec: int, acc: int) -> (int, bool):
    history = set()
    while True:
        if exec in history or exec > len(code):
            return acc, False
        if exec == len(code):
            return acc, True
        history.add(exec)
        exec, acc = execute(code, exec, acc)
        type(exec)


def code_fuzzer(code) -> int:
    i = 0
    while i < len(code):
        if code[i][0] in ["nop", "jmp"]:
            test_code = code.copy()
            if code[i][0] == "nop":
                test_code[i] = ["jmp", code[i][1]]
            elif code[i][0] == "jmp":
                test_code[i] = ["nop", code[i][1]]
            acc, valid = run_code(test_code, 0, 0)
            if valid:
                return acc
        i += 1


# Part 1
code = get_input()
acc, valid = run_code(code, 0, 0)
print("Part 1: {}".format(acc))

# Part 2
acc = code_fuzzer(code)
print("Part 2: {}".format(acc))
