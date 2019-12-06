from intcode_computer import parse_intcode

def part1(init):
    inputs = init.copy()
    inputs[1], inputs[2] = 12, 2
    return parse_intcode(inputs, 0)[0]


def part2(init):
    for i in range(100):
        for j in range(100):
            inputs = init.copy()
            inputs[1], inputs[2] = i, j
            if parse_intcode(inputs, 0)[0] == 19690720:
                return 100 * i + j


with open("day2-input.txt", "r") as f:
    inputs = list(map(int, f.read().split(",")))

print(part1(inputs))
print(part2(inputs))

