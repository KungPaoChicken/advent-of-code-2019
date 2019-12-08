from intcode_computer import parse_intcode

inputs = list(map(int, open("day5-input.txt").read().split(",")))

# inputs = list(map(int, "1002,4,3,4,33".split(",")))

print(parse_intcode(inputs, 0))
