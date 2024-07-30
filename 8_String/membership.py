# Memebership "in" or "not in"
# Returns boolean

my_string = "asdmbvhiuejwvc"

total = 0
for ch in my_string.lower():
    if ch in ("aeiouAEIOU"):
        total += 1

print(total)
