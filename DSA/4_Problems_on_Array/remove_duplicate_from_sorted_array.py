"""
Remove Duplicates from Sorted Array
"""

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# n = len(nums)
# dict = {}
# for i in range(0, n):
#     dict[nums[i]] = 0

# print(dict)

# j = 0 # counter
# for key in dict:
#     nums[j] = key
#     j += 1

# print(len(dict))
# print(j)

# Optimal -  2 pointer way
n = len(nums)
i = 0
j = i + 1
while j < n:
    if nums[j] != nums[i]:
        i += 1
        nums[i], nums[j] = nums[j], nums[i]
    j += 1
print(i + 1)
