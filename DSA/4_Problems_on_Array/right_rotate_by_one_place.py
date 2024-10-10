"""
Right rotate by 1 place.
"""

nums = [5, 9, 8, 1, 8, 6, 1, 7]

temp = nums[-1]
n = len(nums)
for i in range(n - 1, 0, -1):
    nums[i] = nums[i - 1]

nums[0] = temp

print(nums)
