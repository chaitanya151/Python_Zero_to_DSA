n = int(input("Enter the start position: "))
l = int(input("Enter the last position: "))

my_list = []

for i in range(n, l + 1):
    my_list.append(i)

print(my_list[:])
