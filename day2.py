from intcode_computer import str_to_program, parse_intcode


def part1(inputs):
    program = inputs.copy()
    program[1], program[2] = 12, 2
    return parse_intcode(program, 0)[0][0]


def part2(inputs):
    for i in range(100):
        for j in range(100):
            program = inputs.copy()
            program[1], program[2] = i, j
            if parse_intcode(program, 0)[0][0] == 19690720:
                return 100 * i + j


program = str_to_program(open("day2-input.txt", "r").read())

print(part1(program))
print(part2(program))
