nums = [0, 1, 0, 3, 12]
nums2 = [1, 2, 3, 4, 0, 5, 6, 7, 8]

# Brute force -> TC : O(N)
# non_zero_list = []
# n = len(nums)
# for i in range(n):  # O(N)
#     if nums[i] != 0:
#         non_zero_list.append(nums[i])

# nzl = len(non_zero_list)
# for i in range(0, nzl):  # 7 elements
#     nums[i] = non_zero_list[i]
# for i in range(nzl, n):  # 3 elements
#     nums[i] = 0

# print(nums)


# Optimal
def move_zeros(nums: list[int]):
    n = len(nums)
    if n == 1:
        return
    i = 0
    while i < n:
        if nums[i] == 0:
            break
        i += 1
    j = i + 1
    while j < n:
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    return nums


print(move_zeros(nums))
print(move_zeros(nums2))
