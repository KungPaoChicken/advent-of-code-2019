from collections import defaultdict


def set_state(s, k, v):
    s[k] = v
    return s


def set_memory(s, k, v):
    s["memory"][k] = v
    return s


def read_parameter(memory, index, mode, read, relative_base):
    if mode == 0:
        return memory[memory[index]] if read else memory[index]
    elif mode == 1:
        return memory[index]
    else:
        return (
            memory[relative_base + memory[index]]
            if read
            else relative_base + memory[index]
        )


def read_parameters(state, n, modes, rw):
    return [
        read_parameter(
            state["memory"],
            state["ip"] + 1 + i,
            modes[i],
            rw[i],
            state["relative_base"],
        )
        for i in range(n)
    ]


def read_instruction(s):
    instruction = str(s["memory"][s["ip"]])
    opcode = int(instruction[-2:])
    num_parameters = handlers.get(opcode)[0]
    modes = [0] * num_parameters
    if len(instruction) > 2:
        modes = [int(i) for i in instruction[:-2][::-1]]
        modes += [0] * (num_parameters - len(modes))
    return (opcode, modes)


def intcode_input(inputs=[]):
    if inputs:
        return inputs.pop(0)
    return int(input("Input: "))


def intcode_output(p, i, outputs):
    outputs.append(i)
    return p


# Number of parameters, read(1)/write(0) access on each parameter, and function to handle opcode
handlers = {
    1: (3, [1, 1, 0], lambda s, i, j, k: set_memory(s, k, i + j)),
    2: (3, [1, 1, 0], lambda s, i, j, k: set_memory(s, k, i * j)),
    3: (1, [0], lambda s, i: set_memory(s, i, intcode_input(s["inputs"]))),
    4: (1, [1], lambda s, i: intcode_output(s, i, s["outputs"])),
    5: (2, [1, 1], lambda s, x, y: set_state(s, "ip", y if x != 0 else s["ip"] + 3)),
    6: (2, [1, 1], lambda s, x, y: set_state(s, "ip", y if x == 0 else s["ip"] + 3)),
    7: (3, [1, 1, 0], lambda s, i, j, k: set_memory(s, k, 1 if i < j else 0)),
    8: (3, [1, 1, 0], lambda s, i, j, k: set_memory(s, k, 1 if i == j else 0)),
    9: (1, [1], lambda s, i: set_state(s, "relative_base", s["relative_base"] + i)),
    99: (0, [], lambda s: set_state(s, "ip", s["program_end"])),
}


def parse(state, **kwargs):
    inputs = state
    while inputs["ip"] < inputs["program_end"]:
        opcode, modes = read_instruction(inputs)
        handler = handlers.get(opcode)
        parameters = read_parameters(inputs, handler[0], modes, handler[1])
        outputs = handler[2](inputs, *parameters)
        if opcode not in [5, 6]:
            outputs["ip"] += handler[0] + 1
        if kwargs.get("quit_on_output") and opcode == 4:
            return outputs
    return outputs


def init(raw_program):
    program = raw_program.split(",")
    return {
        "memory": defaultdict(int, {k: int(v) for k, v in enumerate(program)}),
        "program_end": len(program),
        "ip": 0,
        "inputs": [],
        "outputs": [],
        "relative_base": 0,
    }
