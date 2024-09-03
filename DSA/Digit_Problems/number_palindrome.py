def number_palindrome(num: int) -> bool:

    n = num
    res = 0
    # Reverse number logic
    while n > 0:
        last = n % 10
        res = (res * 10) + last
        n = n // 10
    # print(type(res))
    print(res)

    return num == res


num = 12344321
print(number_palindrome(num))
