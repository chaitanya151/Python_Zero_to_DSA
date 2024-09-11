"""
use only if we have to return TRUE/FALSE
"""

nums = [2, 3, 4, 11, 6, 8]
target = 15


def two_sum(nums, target):
    n = len(nums)
    nums.sort()
    L = 0
    R = n - 1
    while L < R:
        if nums[L] + nums[R] == target:
            return True
        if nums[L] + nums[R] > target:
            R -= 1
        else:
            L += 1
    return False


print(two_sum(nums, target))
