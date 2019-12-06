def offset_to_coordinate(start, offset):
    shifts = {
        "U": lambda x, y, o: (x, y + o),
        "D": lambda x, y, o: (x, y - o),
        "L": lambda x, y, o: (x - o, y),
        "R": lambda x, y, o: (x + o, y),
    }
    return shifts.get(offset[0])(*start, int(offset[1:]))


def directions_to_coordinates(paths):
    start = (0, 0)
    coordinates = []
    for path in paths:
        end = offset_to_coordinate(start, path)
        coordinates.append([start, end])
        start = end
    return coordinates


def is_vertical(x0, x1):
    return x0 == x1


def linear_intersections(range1, range2):
    return set(range(*range1)).intersection(range(*range2))


def find_intersections(lines1, lines2):
    intersections = []
    for (x0, y0), (x1, y1) in sorted(lines1):
        for (i0, j0), (i1, j1) in sorted(lines2):
            if is_vertical(x0, x1):
                if (min(y0, y1) <= j0 <= max(y0, y1)) and (
                    min(i0, i1) <= x0 <= max(i0, i1)
                ):
                    intersections.append((x0, j0))
            else:
                if (min(j0, j1) <= y0 <= max(j0, j1)) and (
                    min(x0, x1) <= i0 <= max(x0, x1)
                ):
                    intersections.append((i0, y0))
    return intersections


def manhattan_distance(x, y):
    return abs(x) + abs(y)


def wire_distance(lines, x, y):
    distance = 0
    for (x0, y0), (x1, y1) in lines:
        if min(x0, x1) <= x <= max(x0, x1) and min(y0, y1) <= y <= max(y0, y1):
            return distance + abs(y - y0) + abs(x - x0)
        else:
            distance += abs(y1 - y0) + abs(x1 - x0)


with open("day3-input.txt", "r") as f:
    wire1 = f.readline()
    wire2 = f.readline()

lines1 = directions_to_coordinates(wire1.split(","))
lines2 = directions_to_coordinates(wire2.split(","))
intersections = find_intersections(lines1, lines2)
intersections.remove((0, 0))
distances = [manhattan_distance(*i) for i in intersections]
print(min(distances))
wire_distances = [
    wire_distance(lines1, *i) + wire_distance(lines2, *i) for i in intersections
]
print(min(wire_distances))
