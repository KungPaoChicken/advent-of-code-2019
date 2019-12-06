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


