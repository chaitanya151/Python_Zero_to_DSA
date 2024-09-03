num = 1257
# output = 7521
n = num
res = 0
while n > 0:
    last = n % 10
    res = (res * 10) + last
    n = n // 10
# print(type(res))
print(res)
