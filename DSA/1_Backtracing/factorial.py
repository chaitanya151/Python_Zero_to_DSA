n = 0


def factorial(n):
    if (
        n == 1 or n == 0
    ):  # if n==0 is not given then RecursionError: maximum recursion depth exceeded
        return 1
    return n * factorial(n - 1)


print(factorial(n))
