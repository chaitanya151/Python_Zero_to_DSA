# Fibonnaci Number


def foo(index):
    if index == 0:
        return 0
    if index == 1:
        return 1
    return foo(index - 1) + foo(index - 2)


f = foo(6)
print(f)
