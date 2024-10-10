"""
Brute force
"""

nums = [3, 6, 8, 2, 1]
res = []
target = 14


def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1):
            if nums[i] + nums[j] == target:
                return [i, j]


print(two_sum(nums, target))
