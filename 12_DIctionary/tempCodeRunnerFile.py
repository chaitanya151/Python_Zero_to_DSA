for num in my_list:
    # concise way of writing code.
    my_dict[num] = my_dict.get(num, 0) + 1
print(my_dict)