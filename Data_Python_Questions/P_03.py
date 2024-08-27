# Flatten a list and count occurances.


def solve(input_list: list):
    d = {}
    l = []
    for num in input_list:
        if type(num) is list:
            l.extend(solve(num))
        else:
            l.append(num)
    for i in l:
        d[i] = d.get(i, 0) + 1
    return d


input_list = [[1, 2], [3, 4], [2, 3], [5, 1], [7, 9, 2], [7, 1, 6, 8, 9, 0]]
print(solve(input_list))
