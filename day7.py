from intcode_computer import init, parse
from copy import deepcopy
from itertools import permutations


def amplifiers_config1(amplifiers, phase_settings, input_signal=0):
    for i, amplifier in enumerate(deepcopy(amplifiers)):
        amplifier["inputs"] = [phase_settings[i], input_signal]
        outputs = parse(amplifier)
        input_signal = outputs["outputs"][0]
    return outputs["outputs"][0]


def amplifiers_config2(amplifiers, phase_settings, input_signal=0):
    i = 0
    amplifiers = deepcopy(amplifiers)
    for a in range(5):
        amplifiers[a]["inputs"] = [phase_settings[a]]
    amplifiers[0]["inputs"].append(input_signal)
    while True:
        amplifiers[i] = parse(amplifiers[i], quit_before_next_input=True)
        if amplifiers[i]["outputs"]:
            output = amplifiers[i]["outputs"]
            last_output = output[0]
            amplifiers[i]["outputs"] = []
            i = (i + 1) % 5
            amplifiers[i]["inputs"].extend(output)
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


init_state = init(open("day7-input.txt", "r").read())

setup1 = create_setup([deepcopy(init_state) for i in range(5)], amplifiers_config1)
print(max_thruster_signal(setup1, [0, 1, 2, 3, 4]))

setup2 = create_setup([deepcopy(init_state) for i in range(5)], amplifiers_config2)
print(max_thruster_signal(setup2, [5, 6, 7, 8, 9]))
