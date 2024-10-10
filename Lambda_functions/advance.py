# using soretd
people = [("John", 28), ("Anna", 22), ("Mike", 32)]
sorted_by_age = sorted(people, key=lambda x: x[1])
# print(sorted_by_age)

# max
numbers = [(1, 2), (3, 1), (5, 0)]
max_num = max(numbers, key=lambda x: x[1])
min_num = min(numbers, key=lambda x: x[1])
# print(f"max num : {max_num}")
# print(f"min num : {min_num}")

# complex lambda
num = [1, 2, 3, 4, 5, 6]
res_1 = [i for i in num if i % 2 == 0]
# res_2 = list(map(lambda i: i**2, res_1))
res_3 = [(lambda i: i**2)(i) for i in num if i % 2 == 0]
# print(f"res_1:{res_1}")
# print(f"res_2:{res_2}")
# print(f"res_3:{res_3}")

# Sort a list of dictionaries by a specific key using lambda.
data = [
    {"name": "John", "age": 28},
    {"name": "Anna", "age": 22},
    {"name": "Mike", "age": 32},
]
res_1 = sorted(data, key=lambda x: x["age"])
res_2 = sorted(data, key=lambda x: x["age"], reverse=True)
# print(res_1)
# print(res_2)

# Find the longest word in a list of words using max() and a lambda function.
words = ["apple", "banana", "cherry", "blueberry", "grapefruit"]
longest_word = max(words, key=lambda words: len(words))  # longest_word
longest_alpha_word = max(words, key=lambda x: x)  # alphabetically_largest_word

# print(longest_word)

# Create a list of numbers and use reduce() to find the maximum number.
from functools import reduce

num = [3, 6, 7, 4, 22, 36, 9]
max_num = reduce(lambda i, j: i if i > j else j, num)
# print(max_num)
