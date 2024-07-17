num = int(input("Number: "))


def sum_factor(n: int) -> int:
    i = 1
    total = 0
    while i <= num:
        if num % i == 0:
            total += i
        i += 1
    return total


print(sum_factor(num))
