n = int(input("No. of lines: "))


def pattern(n: int):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


pattern(n)
