a = int(input("Number a: "))
b = int(input("Number b: "))

count = 0
if a < b:
    i = a
    j = b
    while i <= j:
        if i % 3 == 0 and i % 5 == 0:
            count += 1
        i += 1
else:
    i = a
    j = b
    while i <= j:
        if i % 3 == 0 and i % 5 == 0:
            count += 1
        i += 1

print(count)
