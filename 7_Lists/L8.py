my_list = [5, -8, 10, -15, 2, -4, 95, -34, 25, 100]

# Max output = 95

# maxi = 0 is not use because
# For lists containing all negative numbers,
# initializing maxi to 0 would result in an incorrect maximum value.

maxi = float("-inf")
n = len(my_list)
for i in range(0, n):
    if my_list[i] > maxi:
        maxi = my_list[i]
print(f"Max number -> {maxi}")
