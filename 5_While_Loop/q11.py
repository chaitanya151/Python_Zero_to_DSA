def sum_of_square(n: int) -> int:
    i = 1
    sum_of_square = 0
    square = 0
    while i <= n:
        square = i**2
        print(f"square -> {square}")
        sum_of_square += square
        print(f"sum_of_square -> {sum_of_square}")
        i += 1
        print(f"i -> {i}")

    return sum_of_square


n = int(input("Number -> "))
container_1 = sum_of_square(n)
print(container_1)
