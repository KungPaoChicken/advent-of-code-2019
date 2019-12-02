import math


def fuel_requirement(mass):
    fr = math.floor(mass / 3) - 2
    if fr <= 0:
        return 0
    return fr + fuel_requirement(fr)

with open("day1-input.txt", "r") as f:
    fuel_requirements = 0
    for mass in f:
        fuel_requirements += fuel_requirement(int(mass))

print(fuel_requirements)
