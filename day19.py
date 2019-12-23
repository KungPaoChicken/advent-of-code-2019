from intcode_computer import init, parse
from copy import deepcopy


def is_tractor_beam(x, y):
    p = deepcopy(program)
    p["inputs"] = [x, y]
    return parse(p)["outputs"][0]


def tractor_beam_area(x, y):
    total = 0
    for j in range(y):
        for i in range(x):
            total += is_tractor_beam(i, j)
    return total


from time import sleep


def tractor_beam_fitting(w, h):
    # Set starting point larger to speed up search
    x0, y = 469, 299
    corner = {}
    while True:
        beam = is_tractor_beam(x0, y)
        if beam:
            x1 = x0 + w - 1
            if is_tractor_beam(x1, y):
                while True:
                    x1 += 1
                    if not is_tractor_beam(x1, y):
                        break
                corner[y] = (x0, x1 - 1)
                miny, y1 = min(corner.keys()), max(corner.keys())
                if y1 - miny >= h:
                    y0 = y1 - h + 1
                    width = corner.get(y0, (0, 0))[1] - corner[y1][0]
                    # print(x0, y0, ", width:", width)
                    if width >= w - 1:
                        return corner[y0][1] - w + 1, y0
            y += 1
        else:
            # assuming beam on next row always startx at least 1 block to the right
            x0 += 1


program = init(open("day19-input.txt", "r").read())

print(tractor_beam_area(50, 50))

x, y = tractor_beam_fitting(100, 100)
print(x * 10000 + y)
