from intcode_computer import str_to_program, parse_intcode

inputs = str_to_program(open("day5-input.txt").read())

# Input 1
print("Part 1: Input 1")
parse_intcode(inputs.copy(), 0, disable_jumps=True)

# Input 5
print("Part 2: Input 5")
parse_intcode(inputs.copy(), 0)
