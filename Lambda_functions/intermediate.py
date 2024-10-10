# using map()
num = [1, 2, 3, 4, 5]
square = list(map(lambda x: x**2, num))
# print(square)

# filter
num = [1, 2, 3, 4, 5, 6, 7, 8]
num_filter = list(filter(lambda x: x % 2 == 0, num))
# print(f"Filter : {num_filter}")

# reduce
from functools import reduce

num = [1, 2, 3, 4]
num_reduce = reduce(lambda x, y: x + y, num)
# print(f"Reduce : {num_reduce}")

# Use filter() with a lambda function to get
# only the words from a list that have more than 4 letters.
my_list = ["Johnny", "Anna", "Mikey"]
word = list(filter(lambda x: len(x) % 4 > 0, my_list))
# print(word)

# Use reduce() to find the product of all numbers in a list.
from functools import reduce

num = [1, 2, 3, 4]
res = reduce(lambda x, y: x * y, num)
# print(res)
