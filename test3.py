"""
Given a list of integers. 
Find frequency of elements in the list using dictionary comprehension
"""

nums = [6, 7, 10, 7, 6, 6, 4, 3, 3, 7, 7]
d = {num: nums.count(num) for num in nums}
print(d)
