inputs = (356261, 846303 + 1)


def is_increasing(number):
    s = str(number)
    for i in range(len(s) - 1):
        if s[i + 1] < s[i]:
            return False
    return True


def has_double(number):
    s = str(number)
    for i in range(len(s) - 1):
        if s[i + 1] == s[i]:
            return True
    return False


def is_password(number):
    return is_increasing(number) and has_double(number)


print(len(list(filter(is_password, range(*inputs)))))
