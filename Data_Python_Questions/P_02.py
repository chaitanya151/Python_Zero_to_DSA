"""
find the items greater than itself 
after its index in a python list.

input = [99,28,12,55,13,15,76,99]

"""

input = [99, 28, 12, 55, 13, 15, 76, 99]

n = len(input)
i = 0
j = 0

for i in range(n):
    count = 0
    greater_list = []
    for j in range(i, n):
        if input[j] > input[i]:
            greater_list.append(input[j])
            count += 1
    i += 1
    print(i, count, greater_list)
