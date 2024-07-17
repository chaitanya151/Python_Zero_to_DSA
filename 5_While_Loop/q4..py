i = 5674
j = 10983

count = 0
count_2 = 0
while i <= j:
    if i % 7 == 0:
        count += 1
    if (i % 2 == 0) and (i % 7 == 0):
        count_2 += 1
    i += 1
print(f"count : {count}")
print(f"count_2 : {count_2}")
