from copy import deepcopy

a = [1, 2, 3, 4, 5, 6, 7]
a = [1, 2, 3, [88, 9, 44], 5, 6]  # Use to understand the deep copy

# b = a # Run this value first
# b = a.copy()  # Then shallow copy
b = deepcopy(a)  # Deep copy to change the address of the inner mutable.

print(f"a -> {id(a)}")
print(f"b -> {id(b)}")

print(f"a = {a}")
print(f"b = {b}")

b[0] = 100
b[3][0] = 100

print(f"a = {a}")
print(f"b = {b}")
