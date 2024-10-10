# calculate power
def func(base, power):
    if power == 0 or base == 1:
        return 1
    if power == 1:
        return base
    return base * func(base, power - 1)


print(func(5, 5))

# Time complexity - O(power + 1) => O(power)
