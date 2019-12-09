from intcode_computer import str_to_program, parse_intcode

program = str_to_program(open("day5-input.txt").read())

_, part1 = parse_intcode(program.copy(), 0, [1], [], disable_jumps=True)
print(part1)
_, part2 = parse_intcode(program.copy(), 0, [5], [])
print(part2)
