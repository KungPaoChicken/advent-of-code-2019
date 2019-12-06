def is_increasing(number):
    s = str(number)
    for i in range(len(s) - 1):
        if s[i + 1] < s[i]:
            return False
    return True


from collections import Counter


def has_double(number):
    c = Counter(str(number))
    return max(c.values()) > 1


def has_at_least_one_double(number):
    c = Counter(str(number))
    return 2 in c.values()


def is_part1_password(number):
    return is_increasing(number) and has_double(number)


inputs = (356261, 846303 + 1)

part1_passwords = list(filter(is_part1_password, range(*inputs)))
print(len(part1_passwords))
print(len(list(filter(has_at_least_one_double, part1_passwords))))

