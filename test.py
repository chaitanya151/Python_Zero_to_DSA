"""
Given a List of n integers and a number k, 
find the pairs of numbers in the list such that 
the difference between the pair is k. 
Find the optimal solution with and without extra storage
give an example and solve.
"""

nums = [1, 5, -3, 4, 2]
k = 2
n = len(nums)
pairs = []
for i in range(0, n):
    for j in range(0, n):
        diff = abs(nums[j] - nums[i])
        if diff == k:
            pairs.append((nums[i], nums[j]))

print(pairs)
