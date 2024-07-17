n = int(input("Lines: "))

for i in range(n, 0, -1):
    for j in range(1, i):
        print("_", end=" ")
    for k in range(i, n + 1):
        print(i, end=" ")
    print()
