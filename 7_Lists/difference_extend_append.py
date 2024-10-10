# Difference between extend and append.
fruits = ["apple", "banana"]
more_fruits = ["cherry", "orange"]

fruits.extend(more_fruits)
print(f"With extend function : {fruits}")

fruits = ["apple", "banana"]
fruits.append(more_fruits)
print(f"With append function : {fruits}")
