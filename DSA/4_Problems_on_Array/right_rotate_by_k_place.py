"""
Right rotate by "k" place.
Use reverse array function 3 times.
First iteration will roatate the k elements
Second iteration will rotate the k-n elemnts
Third will rotate whole array to give the output.
"""


def reverse_nums(nums: list[int], l: int, r: int) -> list[int]:

    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r += 1
    return nums


def rotate(nums: list[int], k: int) -> list[int]:
    n = len(nums)
    k %= n

    reverse_nums(nums, n - k, n - 1)
    reverse_nums(nums, 0, n - k - 1)
    reverse_nums(nums, 0, n - 1)

    return nums


nums = [5, 9, 8, 1, 8, 6, 1, 7]

print(rotate(nums, 3))
