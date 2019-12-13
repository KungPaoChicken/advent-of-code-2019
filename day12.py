import re
from math import gcd
from collections import defaultdict


def read_scan(scan):
    return [
        (
            [
                int(m)
                for m in re.match(
                    r"<x=([-0-9]+), y=([-0-9]+), z=([-0-9]+)>", line
                ).groups()
            ],
            [0, 0, 0],
        )
        for line in scan.split("\n")
    ]


def gravity(i, j):
    if i == j:
        return (0, 0)
    elif i < j:
        return (1, -1)
    else:
        return (-1, 1)


def step(moons):
    dv = []
    new_moons = []
    for i in range(len(moons)):
        ms = moons.copy()
        p0, _ = ms.pop(i)
        dv0, _ = zip(*[zip(*[gravity(*a) for a in zip(p0, p1)]) for p1, v1 in ms])
        dv.append([sum(v) for v in zip(*dv0)])
    for i, (p, v) in enumerate(moons):
        v = [v[j] + dv[i][j] for j in range(3)]
        p = [p[j] + v[j] for j in range(3)]
        new_moons.append((p, v))
    return new_moons


def simulate(init_state, steps):
    s = init_state
    for _ in range(steps):
        s = step(s)
    return s


def total_energy(moons):
    total = 0
    for pos, vel in moons:
        pot = sum([abs(p) for p in pos])
        kin = sum([abs(v) for v in vel])
        total += pot * kin
    return total


# https://stackoverflow.com/a/42472824
def lcd(*args):
    lcm = args[0]
    for i in args[1:]:
        lcm *= i // gcd(lcm, i)
    return lcm


# TL;DR: Study linear algebra
# https://en.wikipedia.org/wiki/Isomorphism

# Assumptions of the solution:
# 1. The universe comes back to the initial state (t=0), no need to check other states
# 2. Axes are independent
# 3. The period of all axes is the least common multiple of individual axes
# 4. At half the period, all velocities are 0

# Links
# 1: https://old.reddit.com/r/adventofcode/comments/e9vfod/2019_day_12_i_see_everyone_solving_it_with_an/
# 2: https://old.reddit.com/r/adventofcode/comments/e9wcyt/day_12_still_stumped_on_part_2/famagy0/
# 2, 3: https://old.reddit.com/r/adventofcode/comments/e9r2sz/day12_part_2_totally_stuck_on_how_to_approach_this/
# 4: https://old.reddit.com/r/adventofcode/comments/e9nqpq/day_12_part_2_2x_faster_solution/
def period(init_state):
    init_v = list(zip(*list(zip(*init_state))[1]))
    v_periods = defaultdict(list)

    s = init_state
    i = 0
    while True:
        s = step(s)
        i += 1

        v = list(zip(*list(zip(*s))[1]))
        for j in range(3):
            if init_v[j] == v[j]:
                v_periods[j].append(i)

        if all(j in v_periods for j in [0, 1, 2]):
            break

    return lcd(*(v[0] for v in v_periods.values())) * 2


init_state = read_scan(open("day12-input.txt").read())

part1 = init_state.copy()
print(total_energy(simulate(part1, 1000)))

part2 = init_state.copy()
print(period(part2))
