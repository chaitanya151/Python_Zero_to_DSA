n = int(input("No. of lines: "))


def pattern(n: int):
    for i in range(1, n + 1):
        for j in range(n, i - 1, -1):
            print(j, end=" ")
        print()


pattern(n)
