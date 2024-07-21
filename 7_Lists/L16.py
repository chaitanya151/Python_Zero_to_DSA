"""
Make two lists of same length and pass it ti a function.
Return a third list where each element is the sum 
of index.

output - [68,36,15,10,7,10]
"""

lst1 = [10, 25, 30, -10, 1, 9]
lst2 = [58, 11, -15, 20, 6, 1]


def addition(lst1, lst2):
    n = len(lst1)
    result = []
    for index in range(0, n):
        total = lst1[index] + lst2[index]
        result.append(total)
    return result


ans = addition(lst1, lst2)
print(ans)
