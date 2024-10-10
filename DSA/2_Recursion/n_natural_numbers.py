# sum of n natural numbers
# using parameterized recursion.


def foo(i, sum):
    if i < 1:
        print(sum)
        return
    foo(i - 1, sum + i)


foo(4, 0)
