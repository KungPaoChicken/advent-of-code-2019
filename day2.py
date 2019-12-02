def s(l, i, v):
    l[i] = v
    return l


def parse_intcode(inputs, ip):
    if ip >= len(inputs):
        return inputs
    functions = {
        1: lambda x, i: (s(x, x[i + 3], x[x[i + 1]] + x[x[i + 2]]), i + 4),
        2: lambda x, i: (s(x, x[i + 3], x[x[i + 1]] * x[x[i + 2]]), i + 4),
        99: lambda x, i: (x, len(x)),
    }
    return parse_intcode(*functions.get(inputs[ip])(inputs, ip))


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

