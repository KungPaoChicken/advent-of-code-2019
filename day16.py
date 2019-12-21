from itertools import cycle


def pattern(i):
    new_pattern = [x for p in [0, 1, 0, -1] for x in [p] * i]
    return cycle(new_pattern)


def fft(inputs):
    l = len(inputs)
    inputs = [int(i) for i in inputs]
    return "".join(
        [
            str(
                sum(
                    [k for j in range(i, l, 4 * (i + 1)) for k in inputs[j : j + i + 1]]
                )
                - sum(
                    [
                        k
                        for j in range(i + 2 * (i + 1), l, 4 * (i + 1))
                        for k in inputs[j : j + i + 1]
                    ]
                )
            )[-1]
            for i in range(l)
        ]
    )


def decode(inputs):
    o = inputs[-1]
    for i in range(-2, -len(inputs) - 1, -1):
        o += str(int(o[-1]) + int(inputs[i]))[-1]
    return "".join(o[::-1])


def repeat(f, inputs, n):
    for _ in range(n):
        inputs = f(inputs)
    return inputs


signal = open("day16-input.txt", "r").read()
part1 = signal
print(repeat(fft, part1, 100)[:8])

offset = int(signal[:7])
real_signal = (signal * 10000)[offset:]
print(repeat(decode, real_signal, 100)[:8])
