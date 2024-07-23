# a = (1, 2, 3)
# print(a)
# print(type(a))

# Unpacking

# a, b, c = (1, 2, 3)

# print(a)
# print(b)
# print(c)

# a, b, c, d = (1, 2, 3, "A")
# print(a, b, c, d)

# Applicable in lists too
# x, y, z = [10, 20, "D"]
# print(x, y, z)

# a = 76, 45, 33, 78
# print(a)
# print(type(a))

a = (67,)
# single element tuple
x, y, z = 57, 34, 98

# Spread operator
a, b, *c = [1, 2, 3, 4, 5, 6, 7]
x, y, *z = [1, 2, 3, 4, 5, 6, 7]
print(f"{a = }")
print(f"{b = }")
print(f"{c = }")
print("========")
print(f"{x = }")
print(f"{y = }")
print(f"{z = }")
