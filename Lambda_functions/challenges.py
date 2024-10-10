# Square of a number
square = lambda x: x**2
# print(square(5))

# Check if a number is even or odd
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
# print(is_even(4))

# Add 10 to a number
add_ten = lambda x: x + 10
# print(add_ten(2))


# Sort a list of tuples by the second value:
pairs = [(1, 3), (2, 1), (4, 5), (9, 0)]
sort_nums = sorted(pairs, key=lambda x: x[1])
# print(sort_nums)

# Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
filter_num = list(filter(lambda x: x % 2 == 0, numbers))
# print(filter_num)

# Convert a list of strings to uppercase
words = ["apple", "banana", "grape"]
uppercase = list(map(lambda x: x.upper(), words))
# print(uppercase)

# Find the second largest number in a list using reduce()
from functools import reduce

numbers = [1, 5, 8, 10, 2, 7, 6]
res = reduce(lambda x, y: y if x < y else x, numbers)
# print(res)

# Group numbers by even and odd using filter() and a lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
odds = list(filter(lambda x: x % 2 != 0, numbers))
# print(evens)
# print(odds)

# Sort a list of strings by length and then alphabetically:
words = ["apple", "cat", "banana", "dog", "grape", "carrot"]
sort_list = sorted(words, key=lambda x: (len(x), x))
# print(sort_list)

# Sort a list of dictionaries by multiple keys
# Write a lambda function that sorts a list of dictionaries
# by both age (ascending) and name (alphabetically).
people = [
    {"name": "John", "age": 28},
    {"name": "Anna", "age": 22},
    {"name": "Mike", "age": 32},
    {"name": "Anna", "age": 30},
]

sortt_dict = sorted(people, key=lambda x: (x["age"], ["name"]))
# print(sortt_dict)

# Sorting by the number of vowels in a string: Write a lambda
# function to sort a list of words based on the number of vowels in each word.
words = ["apple", "banana", "cherry", "date", "grape"]
vowels = "aeiou"
sorted_by_vowels = sorted(
    words, key=lambda word: sum(1 for char in word if char.lower() in vowels)
)
print(sorted_by_vowels)
