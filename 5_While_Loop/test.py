n = 368
total = 0
i = 1

while i <= n:
    if n % i == 0:
        total = total + i
    i = i + 1
print(total)
