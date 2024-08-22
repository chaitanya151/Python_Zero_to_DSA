# factorial of a number


def fac(num):
    if num == 0 or num == 1:  # base case
        return 1
    return num * fac(num - 1)


f = fac(5)
print(f)
