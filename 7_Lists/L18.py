l1_even = []
l2_even = []
o1_odd = []
o2_odd = []

my_list = [10, 23, 31, 46, 8, 9]

n = len(my_list)
for index in range(0, n):
    if my_list[index] % 2 != 0:
        l1_even.append(my_list[index])
    else:
        o1_odd.append(my_list[index])

print(l1_even)
print(o1_odd)
