import re


def count_parents(o):
    c = 0
    while orbits[o] != "":
        o = orbits[o]
        c += 1
    return c


def create_orbits(orbit_map):
    objects = set(re.split(r"[\)\n]", orbit_map))
    orbits = {o: "" for o in objects}
    for orbit in orbit_map.split("\n"):
        i, j = orbit.split(")")
        orbits[j] = i
    return orbits


orbit_map = open("day6-input.txt", "r").read()
orbits = create_orbits(orbit_map)

# Part 1: Sum of orbital transfers
total = 0
for o in orbits.keys():
    total += count_parents(o)

print(total)

# Part 2
