# my_list = [57, 88, 9, "C", True, 78.56]

# print(my_list[-1])
# print(my_list[0])

# Define the list
my_list = [5, -8, 10, -15, 2, -4, 95, -34, 25, 100]

# Get the length of the list
n = len(my_list)
print(n)

# Iterate through the list in reverse order and print each element
for i in range(n - 1, -1, -1):
    print(my_list[i], end=" ")
