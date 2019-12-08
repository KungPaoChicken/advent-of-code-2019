def s(l, i, v):
    l[i] = v
    return l


def read_parameters(x, i, n, ms):
    return [x[i + 1 + j] if ms[j] else x[x[i + 1 + j]] for j in range(n)]


def cf(n, f):
    return lambda x, i: (
        f(x, *read_parameters(x, i, n, read_instruction(x, i)[1])),
        i + n + 1,
    )


parameter_modes = {1: [0, 0, 1], 2: [0, 0, 1], 3: [1], 4: [0]}


def read_instruction(x, i):
    instruction = str(x[i])

    if len(instruction) > 2:
        opcode = instruction[-2:]
        modes = [int(i) for i in instruction[:-2][::-1]] + parameter_modes.get(
            int(opcode)
        )[len(instruction) - 2 :]
    else:
        opcode = instruction
        modes = parameter_modes.get(int(opcode))
    return (int(opcode), modes)


def intcode_input():
    return 1


def intcode_output(x, i):
    print(i)
    return x


def parse_intcode(inputs, ip):
    if ip >= len(inputs):
        return inputs
    functions = {
        1: cf(3, lambda x, i, j, k: s(x, k, i + j)),
        2: cf(3, lambda x, i, j, k: s(x, k, i * j)),
        3: cf(1, lambda x, i: s(x, i, intcode_input())),
        4: cf(1, lambda x, i: intcode_output(x, i)),
        99: lambda x, i: (x, len(x)),
    }
    instruction = read_instruction(inputs, ip)[0]
    return parse_intcode(*functions.get(instruction)(inputs, ip))
