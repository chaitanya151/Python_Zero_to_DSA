# Sum of N natural numbers


def func(num):
    if num == 1:
        return 1
    return num + func(num - 1)


x = func(10)
print(x)
