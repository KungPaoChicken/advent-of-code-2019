def set_state(s, k, v):
    s[k] = v
    return s


def set_memory(s, k, v):
    s["memory"][k] = v
    return s


def read_parameter(memory, index, mode, relative_base):
    if mode == 0:
        return memory[memory[index]]
    elif mode == 1:
        return memory[index]
    else:
        relative_base += index
        return memory[memory[relative_base]]


def read_parameters(state, n, modes):
    return [
        read_parameter(
            state["memory"], state["ip"] + 1 + i, modes[i], state["relative_base"]
        )
        for i in range(n)
    ]


def read_instruction(s):
    instruction = str(s["memory"][s["ip"]])
    opcode = int(instruction[-2:])
    # print(s["ip"], instruction, opcode)
    modes = handlers.get(opcode)[1]
    if len(instruction) > 2:
        modes = [int(i) for i in instruction[:-2][::-1]] + modes[len(instruction) - 2 :]
    return (opcode, modes)


def intcode_input(inputs=[]):
    if inputs:
        return inputs.pop(0)
    return int(input("Input: "))


def intcode_output(p, i, outputs):
    outputs.append(i)
    return p


handlers = {
    1: (3, [0, 0, 1], lambda s, i, j, k: set_memory(s, k, i + j)),
    2: (3, [0, 0, 1], lambda s, i, j, k: set_memory(s, k, i * j)),
    3: (1, [1], lambda s, i: set_memory(s, i, intcode_input(s["inputs"]))),
    4: (1, [0], lambda s, i: intcode_output(s, i, s["outputs"])),
    5: (2, [0, 0], lambda s, x, y: set_state(s, "ip", y if x != 0 else s["ip"] + 3)),
    6: (2, [0, 0], lambda s, x, y: set_state(s, "ip", y if x == 0 else s["ip"] + 3)),
    7: (3, [0, 0, 1], lambda s, i, j, k: set_memory(s, k, 1 if i < j else 0)),
    8: (3, [0, 0, 1], lambda s, i, j, k: set_memory(s, k, 1 if i == j else 0)),
    9: (1, [0], lambda s, i: set_state(s, "relative_base", s["relative_base"] + i)),
    99: (0, [], lambda s: set_state(s, "ip", s["program_end"])),
}


def parse(state, **kwargs):
    inputs = state
    if inputs["ip"] >= inputs["program_end"]:
        return inputs

    opcode, modes = read_instruction(inputs)
    # print(inputs["ip"], opcode)
    handler = handlers.get(opcode)
    parameters = read_parameters(inputs, handler[0], modes)
    # print(inputs["memory"].values())
    outputs = handler[2](inputs, *parameters)
    # print(outputs["memory"].values())
    if opcode not in [5, 6]:
        outputs["ip"] += handler[0] + 1
    # print(inputs["ip"], outputs["ip"])
    if kwargs.get("quit_on_output") and opcode == 4:
        return outputs
    return parse(outputs, **kwargs)


def init(raw_program):
    program = raw_program.split(",")
    return {
        "memory": {k: int(v) for k, v in enumerate(program)},
        "program_end": len(program),
        "ip": 0,
        "inputs": [],
        "outputs": [],
        "relative_base": 0,
    }
