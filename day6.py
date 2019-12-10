def get_parents(o):
    parents = []
    while orbits[o] != "":
        o = orbits[o]
        parents.append(o)
    return parents


def create_orbits(orbit_map):
    pairs = [pair.split(")") for pair in orbit_map.split("\n")]
    objects = set(i for p in pairs for i in p)
    orbits = {o: "" for o in objects}
    for i, j in pairs:
        orbits[j] = i
    return orbits


orbit_map = open("day6-input.txt", "r").read()
orbits = create_orbits(orbit_map)

total = sum(map(lambda o: len(get_parents(o)), orbits.keys()))
print(total)

# Part 2
# Start from the object YOU is orbiting at, to the object SAN is orbiting at
# So there is no need to add 1 to make up for the one common object removed with symmetric difference
print(len(set(get_parents("YOU")).symmetric_difference(get_parents("SAN"))))
