"""
Better
"""

nums = [1, 1, 0, 2, 1, 0, 0, 2, 2, 1, 2]
n = len(nums)
hash_map = {}
for num in nums:
    hash_map[num] = hash_map.get(num, 0) + 1
for i in range(0, hash_map[0]):
    nums[i] = 0
for i in range(hash_map[0], (hash_map[0] + hash_map[1])):
    nums[i] = 1
for i in range((hash_map[0] + hash_map[1]), n):
    nums[i] = 2
print(nums)
