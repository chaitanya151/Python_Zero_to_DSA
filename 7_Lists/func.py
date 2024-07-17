my_list = [1, 2, 5, 7, 9, 5]
# print(sum(my_list))
# print(max(my_list))
# print(min(my_list))
# print(len(my_list))

n = len(my_list)

# for i in range(0, n):
#     print(my_list[i])
for i in range(n - 1, -1, -1):
    print(my_list[i])
