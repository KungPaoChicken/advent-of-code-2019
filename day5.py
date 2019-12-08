from intcode_computer import parse_intcode

inputs = list(map(int, open("day5-input.txt").read().split(",")))

# Input 1
print("Part 1: Input 1")
parse_intcode(inputs.copy(), 0, disable_jumps=True)

# Input 5
print("Part 2: Input 5")
parse_intcode(inputs.copy(), 0)
