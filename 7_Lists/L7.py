my_list = [100, -8, 10, -15, 2, -4, 95, -34, 25]

n = len(my_list)
H = 0

for index in range(n - 1):
    print(my_list[index], end=" ")
    if my_list[index] >= my_list[index + 1]:
        H1 = my_list[index]
    if H1 >= my_list[index + 1]:
        H = H1
    else:
        H = my_list[index + 1]

print(f"Highest num -> {H}")
