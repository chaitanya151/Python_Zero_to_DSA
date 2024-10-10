"""
TC -> O(N^2) SC -> O(1)
"""

arr = [5, 7, 8, 1, 9, 3, 2]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print(arr)
