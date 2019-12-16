from intcode_computer import init, parse
from copy import deepcopy
from collections import defaultdict


def next_location(location, face, direction):
    faces = ["U", "R", "D", "L"]
    funcs = [
        lambda x, y: (x, y + 1),
        lambda x, y: (x + 1, y),
        lambda x, y: (x, y - 1),
        lambda x, y: (x - 1, y),
    ]
    f0 = faces.index(face)
    f1 = (f0 + 1 if direction else f0 - 1) % len(faces)
    return funcs[f1](*location), faces[f1]


def paint_hull(state, start_white=False):
    hull = defaultdict(int)
    location = (0, 0)
    face = "U"
    hull[location] = 1 if start_white else 0
    while not state.get("halt"):
        state["inputs"] = [hull[location]]
        state = parse(state, quit_before_next_input=True)
        colour, direction = state["outputs"][-2:]
        hull[location] = colour
        location, face = next_location(location, face, direction)
    return hull


def visualise_hull(hull):
    x, y = zip(*hull.keys())
    minx, miny, maxx, maxy = abs(min(x)), abs(min(y)), max(x), max(y)
    hull = {(x + minx, y + miny): c for (x, y), c in hull.items()}
    for y in range(maxy + miny, -1, -1):
        s = ""
        for x in range(maxx + minx):
            s += "#" if hull.get((x, y)) else " "
        print(s)


init_state = init(open("day11-input.txt", "r").read())

print(len(paint_hull(deepcopy(init_state)).keys()))

visualise_hull(paint_hull(deepcopy(init_state), start_white=True))
