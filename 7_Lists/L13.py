my_list = [3, 8, 7, 3, 5, 5, 5, 5, 3, 8, 3, 3, 3, 1, 3, 8, 9, 6, 7, 8, 9]
result = []


for num in my_list:
    if my_list.count(num) > 3:
        if num not in result:
            result.append(num)

print(result)
