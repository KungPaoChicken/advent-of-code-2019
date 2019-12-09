from collections import Counter
from functools import reduce


def to_layers(image, width, height):
    return [
        list(map(int, image[i : i + width * height]))
        for i in range(0, len(image), width * height)
    ]


def min_zeros(c1, c2):
    return c1 if c1[0] < c2[0] else c2


def checksum(layers):
    layer_with_fewest_zeros = reduce(
        lambda x, y: min_zeros(Counter(x), Counter(y)), layers
    )
    return layer_with_fewest_zeros[1] * layer_with_fewest_zeros[2]


def get_visible_pixel(pixels):
    for p in pixels:
        if p == 0:
            return 0
        elif p == 1:
            return 1
    return 2


def decode_image(layers, width, height):
    return [
        list(map(lambda pixels: get_visible_pixel(pixels), zip(*layers)))[i : i + width]
        for i in range(0, width * height, width)
    ]


def display_image(image):
    display = {0: "██", 1: "░░", 2: "  "}
    for row in image:
        print("".join(map(lambda p: display.get(p, "?"), row)))


image = open("day8-input.txt", "r").read()
width, height = 25, 6
layers = to_layers(image, width, height)
print(checksum(layers))
display_image(decode_image(layers, width, height))
