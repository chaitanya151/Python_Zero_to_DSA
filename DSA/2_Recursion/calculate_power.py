# foo(base, power)


def foo(base, power):
    if power == 0 or (base == 1 and power == 1) or (base == 0 and power == 1):
        return 1
    return base * foo(base, power - 1)


p = foo(5, 3)
print(p)
