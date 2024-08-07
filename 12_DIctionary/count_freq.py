my_list = [4, 5, 6, 4, 4, 3, 2, 3, 3, 10, 4, 8, 9, 9, 10]
"""
{
    key:count
    4:6,
    5:1,
    6:1,
    10:1,
}
"""
my_dict = {}
for num in my_list:
    if num in my_dict:  # checks if key exists, if yes goes inside the loop.
        my_dict[num] = my_dict[num] + 1  # increment the key's value by 1.
    else:
        my_dict[num] = 1
print(my_dict)
