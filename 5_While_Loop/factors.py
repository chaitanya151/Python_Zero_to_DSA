def print_factors(num: int) -> None:
    i = 1
    while i <= num:
        if num % i == 0:
            print(i, end=" ")
        i += 1


print_factors(100)
