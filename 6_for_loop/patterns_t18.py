n = int(input("Lines: "))

for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print(n + 1 - i, end=" ")
    print()
