from intcode_computer import init, parse
from copy import deepcopy


def part1(inputs):
    init_state = deepcopy(inputs)
    init_state["memory"][1], init_state["memory"][2] = 12, 2
    return parse(init_state)["memory"][0]


def part2(inputs):
    for i in range(100):
        for j in range(100):
            init_state = deepcopy(inputs)
            init_state["memory"][1], init_state["memory"][2] = i, j
            if parse(init_state)["memory"][0] == 19690720:
                return 100 * i + j


init_state = init(open("day2-input.txt", "r").read())

print(part1(init_state))
print(part2(init_state))
