from math import atan2, pi, sin, cos
from collections import defaultdict, OrderedDict


def to_coordinates(am):
    return [
        (int(x), int(y))
        for y, l in enumerate(am.split("\n"))
        for x, c in enumerate(l)
        if c == "#"
    ]


# General idea is to compare slopes
# atan (inverse tangent) can find the angle of a triangle from shorter sides
# atan2 takes 2 arguments (y, x) to avoid divide-by-0
# https://old.reddit.com/r/adventofcode/comments/e8mj2w/2019_day_10_part_1_having_a_hard_time_understand/fadv3og/
# https://gamedev.stackexchange.com/a/14603
def line_of_sight(asteroids):
    in_los = {}
    for i in range(len(asteroids)):
        clone = asteroids.copy()
        x0, y0 = clone.pop(i)
        in_los[(x0, y0)] = len(set([atan2(y1 - y0, x1 - x0) for x1, y1 in clone]))
    return in_los


def quadrant_order(x, y):
    return x, y


def sort_atan2(a):
    return a[0] if a[0] >= -pi / 2 else a[0] + 3 * pi


def order(asteroids, origin):
    angles = defaultdict(list)
    clone = asteroids.copy()
    clone.remove(origin)
    x0, y0 = origin
    for x1, y1 in clone:
        angles[atan2(y1 - y0, x1 - x0)].append((x1, y1))
    for a in angles.keys():
        angles[a] = sorted(angles[a], key=lambda c: abs(c[1] - y0) + abs(c[0] - x0))
    sorted_map = OrderedDict(sorted(angles.items(), key=sort_atan2))
    # return sorted_map
    scan = []
    while sorted_map:
        for a in list(sorted_map.keys()):
            scan.append(sorted_map[a].pop(0))
            if not sorted_map[a]:
                del sorted_map[a]
    return scan


asteroids = to_coordinates(open("day10-input.txt", "r").read())

los = line_of_sight(asteroids)
monitoring_station, asteroids_detected = sorted(
    los.items(), key=lambda i: i[1], reverse=True
)[0]
print(asteroids_detected)

order_of_destruction = order(asteroids, monitoring_station)
x, y = order_of_destruction[199]
print(x * 100 + y)
