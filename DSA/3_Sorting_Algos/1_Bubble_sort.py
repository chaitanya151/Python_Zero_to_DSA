"""
Adjecent Swap.
Like bubble.
"""

from typing import List

# For asc

arr = [5, 7, 8, 1, 9, 3, 2]
arr2 = [5, 6, 1, 9, 10, 14, 7]


def bubble_sort(arr: List[int]) -> List[int]:
    l_arr = len(arr)
    print(f"Length of an array : {l_arr}")
    # setting pointer 'i' to second last element to avoid out of index error
    for i in range(l_arr - 2, -1, -1):
        for j in range(0, i + 1):
            if arr[j + 1] > arr[j]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # swap places
    return arr  # returns the sorted array


print(f"bubble sort asec -> {bubble_sort(arr=arr)}")

# for desc


def bubble_sort_desc(arr2: List[int]) -> List[int]:
    l_arr2 = len(arr2)
    print(f"Length of an array : {l_arr2}")
    for i in range(l_arr2 - 1, -1, -1):
        for j in range(0, i - 2):
            if arr2[j] < arr2[j - 1]:
                arr2[j], arr2[j - 1] = arr2[j - 1], arr2[j]  # swap places
    return arr2  # returns the sorted array


print(f"Bubble sort desc -> {bubble_sort_desc(arr2)}")
