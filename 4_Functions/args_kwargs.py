def add(n1, n2, *n3) -> None:
    print(f"n1 -> {n1}")
    print(f"n2 -> {n2}")
    print(f"n3 -> {n3}")
    print(f"n3 -> {sum(n3)}")


# add(10, 20, 30, 40, 50)


def add_args(*num):
    return f"num -> {sum(num)}"


print(add_args(10, 20, 30))
