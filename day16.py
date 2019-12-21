from itertools import cycle, accumulate


def pattern(i):
    return cycle(x for p in (0, 1, 0, -1) for x in (p,) * i)


def fft(inputs):
    l = len(inputs)
    return tuple(
        abs(
            sum(k for j in range(i - 1, l, 4 * i) for k in inputs[j : j + i])
            - sum(k for j in range(i - 1 + 2 * i, l, 4 * i) for k in inputs[j : j + i])
        )
        % 10
        for i in range(1, l + 1)
    )


def decode(inputs):
    return tuple(accumulate(inputs[::-1], lambda a, b: (a + b) % 10))[::-1]


def repeat(f, inputs, n):
    for _ in range(n):
        inputs = f(inputs)
    return inputs


to_str = lambda i: "".join(map(str, i))

signal = tuple(int(s) for s in open("day16-input.txt", "r").read())
part1 = signal
print(to_str(repeat(fft, part1, 100)[:8]))

offset = int("".join(map(str, signal[:7])))
real_signal = tuple((signal * 10000)[offset:])
print(to_str(repeat(decode, real_signal, 100)[:8]))
