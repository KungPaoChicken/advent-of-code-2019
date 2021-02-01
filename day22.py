from itertools import chain
import re


def deal_into_new_stack(cards):
    return tuple(cards[::-1])


def cut(cards, n):
    return tuple(chain(cards[n:], cards[:n]))


def deal_with_increment(cards, n):
    dealt_cards = {}
    for i in range(len(cards)):
        dealt_cards[(i * n) % len(cards)] = cards[i]

    return tuple(c for _, c in sorted(dealt_cards.items(), key=lambda c: c[0]))


def shuffle(cards, orders):
    for line in orders.split("\n"):
        is_cut = re.match(r"cut (-?\d+)", line)
        is_dwi = re.match(r"deal with increment (\d+)", line)
        if line == "deal into new stack":
            cards = deal_into_new_stack(cards)
        elif is_cut:
            cards = cut(cards, int(is_cut.group(1)))
        elif is_dwi:
            cards = deal_with_increment(cards, int(is_dwi.group(1)))
        else:
            print("Unknown line:", line)
    return cards


cards = range(10007)
orders = open("day22-input.txt", "r").read()

print(shuffle(cards, orders).index(2019))

cards = range(119315717514047)
print(shuffle(cards, orders)[:20])
# for i in range(101741582076661):
#     cards = shuffle(cards, orders)

# print(cards[2020])
