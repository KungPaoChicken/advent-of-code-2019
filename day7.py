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
        print("IN ", inputs[i])
        print("MEM ", amplifiers[i][26:29])
        amplifiers[i], ip[i], inputs[i], output = parse_intcode(
            amplifiers[i], ip[i], inputs[i], [], quit_on_output=True
        )
        if not output:
            return input_signal
        print("OUT", output[0])
        inputs[(i + 1) % 5].append(output[0])
        i = (i + 1) % 5


def create_setup(amplifiers, config):
    return lambda c: config(amplifiers, c)


def max_thruster_signal(amplifier_setup, phase_permutations):
    max_signal = 0
    for phase_settings in permutations(phase_permutations):
        output_signal = amplifier_setup(phase_settings)
        max_signal = max(max_signal, output_signal)
    return max_signal


program = str_to_program(open("day7-input.txt", "r").read())

setup1 = create_setup([program] * 5, amplifiers_config1)
print(max_thruster_signal(setup1, [0, 1, 2, 3, 4]))

program = str_to_program(
    "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5"
)
print(amplifiers_config2([program] * 5, [9, 8, 7, 6, 5]))
# program = str_to_program(
#     "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10"
# )
# print(amplifiers_config2([program] * 5, [9, 7, 8, 5, 6]))

setup2 = create_setup([program] * 5, amplifiers_config2)
# print(max_thruster_signal(setup2, [5, 6, 7, 8, 9]))
