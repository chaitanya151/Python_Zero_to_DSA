n = int(input("Number: "))


def line_pattern(n: int) -> None:
    i = 1
    number = 1
    while i <= n:
        print(number)
        number = (number * 10) + 1
        i += 1


line = line_pattern(n)
print(line_pattern)
