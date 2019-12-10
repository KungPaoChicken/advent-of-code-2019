from intcode_computer import str_to_program, parse_intcode
from itertools import permutations


def amplifiers_config1(amplifiers, phase_settings, input_signal=0):
    for i, amplifier in enumerate(amplifiers):
        _, _, _, output = parse_intcode(
            amplifier, 0, [phase_settings[i], input_signal], []
        )
        input_signal = output[0]
    return output[0]


def amplifiers_config2(amplifiers, phase_settings, input_signal=0):
    i = 0
    ip = [0] * 5
    inputs = [[p] for p in phase_settings]
    inputs[0].append(input_signal)
    while True:
        amplifiers[i], ip[i], inputs[i], output = parse_intcode(
            amplifiers[i], ip[i], inputs[i], [], quit_on_output=True
        )
        if output:
            last_output = output[0]
            inputs[(i + 1) % 5].append(output[0])
            i = (i + 1) % 5
            continue
        return last_output


def create_setup(amplifiers, config):
    return lambda c: config(amplifiers, c)


def max_thruster_signal(amplifier_setup, phase_permutations):
    max_signal = 0
    for phase_settings in permutations(phase_permutations):
        output_signal = amplifier_setup(phase_settings)
        max_signal = max(max_signal, output_signal)
    return max_signal


program = str_to_program(open("day7-input.txt", "r").read())

setup1 = create_setup([program.copy() for i in range(5)], amplifiers_config1)
print(max_thruster_signal(setup1, [0, 1, 2, 3, 4]))

setup2 = create_setup([program.copy() for i in range(5)], amplifiers_config2)
print(max_thruster_signal(setup2, [5, 6, 7, 8, 9]))
