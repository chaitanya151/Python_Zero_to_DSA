def pattern(n: int):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


n = int(input("Number of lines: "))
pattern(n)
