import math


def fuel_requirement(mass, part1=False):
    fr = math.floor(mass / 3) - 2
    if part1:
        return fr
    if fr <= 0:
        return 0
    return fr + fuel_requirement(fr)


with open("day1-input.txt", "r") as f:
    masses = f.readlines()

fuel_requirements = 0
print(sum([fuel_requirement(int(mass), part1=True) for mass in masses]))
print(sum([fuel_requirement(int(mass)) for mass in masses]))
