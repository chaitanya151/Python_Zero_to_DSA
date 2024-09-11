from typing import List

"""
Time complexity -> O(n)
n is number of elements in nums

Space complexity -> O(n)
"""


def twoSum(nums: List[int], target: int):
    n = len(nums)
    hash_map = dict()
    for i in range(n):
        remaining = target - nums[i]
        if remaining in hash_map:
            return [hash_map[remaining], i]
        hash_map[nums[i]] = i
        print(hash_map)


nums = [3, 3]
target = 6

print(twoSum(nums, target))
