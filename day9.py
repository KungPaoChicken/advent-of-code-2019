from intcode_computer import init, parse
from copy import deepcopy

init_state = init(open("day9-input.txt", "r").read())

part1 = deepcopy(init_state)
part1["inputs"] = [1]
print(parse(part1)["outputs"])

part2 = deepcopy(init_state)
part2["inputs"] = [2]
print(parse(part2)["outputs"])
