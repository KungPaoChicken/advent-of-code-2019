def s(l, i, v):
    l[i] = v
    return l


def read_parameters(p, i, n, ms):
    return [p[i + 1 + j] if ms[j] else p[p[i + 1 + j]] for j in range(n)]


def cf(n, f):
    return lambda p, ip, inputs: (
        f(p, *read_parameters(p, ip, n, read_instruction(p, ip)[1])),
        ip + n + 1,
        inputs,
    )


def cf2(n, f):
    return lambda p, ip, inputs: (
        p,
        f(ip, *read_parameters(p, ip, n, read_instruction(p, ip)[1])),
        inputs,
    )


parameter_modes = {
    1: [0, 0, 1],
    2: [0, 0, 1],
    3: [1],
    4: [0],
    5: [0, 0],
    6: [0, 0],
    7: [0, 0, 1],
    8: [0, 0, 1],
}


def read_instruction(p, i):
    instruction = str(p[i])

    if len(instruction) > 2:
        opcode = instruction[-2:]
        modes = [int(i) for i in instruction[:-2][::-1]] + parameter_modes.get(
            int(opcode)
        )[len(instruction) - 2 :]
    else:
        opcode = instruction
        modes = parameter_modes.get(int(opcode))
    return (int(opcode), modes)


def intcode_input(inputs=[]):
    if inputs:
        return inputs.pop(0)
    return int(input("Input: "))


def intcode_output(p, i):
    print(i)
    return p


def parse_intcode(program, ip, inputs=[], disable_jumps=False):
    if ip >= len(program):
        return program
    functions = {
        1: cf(3, lambda p, i, j, k: s(p, k, i + j)),
        2: cf(3, lambda p, i, j, k: s(p, k, i * j)),
        3: cf(1, lambda p, i: s(p, i, intcode_input(inputs))),
        4: cf(1, lambda p, i: intcode_output(p, i)),
        5: cf2(2, lambda ip, x, y: y if x != 0 else ip + 3),
        6: cf2(2, lambda ip, x, y: y if x == 0 else ip + 3),
        7: cf(3, lambda p, i, j, k: s(p, k, 1 if i < j else 0)),
        8: cf(3, lambda p, i, j, k: s(p, k, 1 if i == j else 0)),
        99: lambda p, i, inputs: (p, len(p), inputs),
    }
    if disable_jumps:
        for i in [5, 6, 7, 8]:
            functions.pop(i)
    instruction = read_instruction(program, ip)[0]
    return parse_intcode(*functions.get(instruction)(program, ip, inputs))


def str_to_program(string):
    return list(map(int, string.split(",")))
