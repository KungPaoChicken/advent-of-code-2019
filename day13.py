from intcode_computer import init, parse
from copy import deepcopy
from collections import defaultdict, Counter


def print_board(draw_instructions):
    screen = defaultdict(int)
    for x, y, t in draw_instructions:
        screen[(x, y)] = t

    symbols = [" ", ".", "#", "_", "O"]
    print("SCORE", screen[(-1, 0)])
    for y in range(19):
        p = ""
        for x in range(37):
            p += symbols[screen[(x, y)]]
        print(p)


def play(game, visualise=False):
    game["memory"][0] = 2
    joystick = num_blanks = score = 0
    while True:
        game["inputs"] = [joystick]
        game = parse(game, quit_before_next_input=True)
        outputs = game["outputs"]
        draw_instructions = defaultdict(list)
        len_blanks = 0
        for i in range(0, len(outputs), 3):
            x, y, t = outputs[i : i + 3]
            if x == -1 and y == 0:
                score = t
            elif t == 0:
                len_blanks += 1
            elif t == 3:
                paddle = x
            elif t == 4:
                ball = x
        if num_blanks == len_blanks:
            return score
        num_blanks = len_blanks
        if paddle < ball:
            joystick = 1
        elif paddle > ball:
            joystick = -1
        else:
            joystick = 0
        if visualise:
            print_board(draw_instructions)


game = init(open("day13-input.txt", "r").read())

outputs = parse(deepcopy(game))["outputs"]
draw_instructions = [outputs[x : x + 3] for x in range(0, len(outputs), 3)]
print(len([None for _, _, t in draw_instructions if t == 2]))

print(play(deepcopy(game)))
