from intcode_computer import init, parse
from copy import deepcopy

init_state = init(open("day5-input.txt").read())

part1_init = deepcopy(init_state)
part1_init["inputs"] = [1]
print(parse(part1_init)["outputs"])

part2_init = deepcopy(init_state)
part2_init["inputs"] = [5]
print(parse(part2_init)["outputs"])
