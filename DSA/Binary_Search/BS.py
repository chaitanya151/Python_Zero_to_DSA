num = [2, 4, 6, 7, 10, 11, 16, 18, 21]
high = len(num) - 1
target = 6


def binary_search(num, low, high):
    n = len(num)
    while low <= high:
        mid = (low + high) // 2
        if num[mid] == target:
            return num[mid]
        elif target < num[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


print(binary_search(num, 0, high))
