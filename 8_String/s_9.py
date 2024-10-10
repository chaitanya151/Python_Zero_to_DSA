"""
Avoid Spaces in string length
"""

test_str = "geeksforgeeks 33 best"

count = 0
for ch in test_str:
    if ch != " ":
        count += 1
print(f"Total characters are : {count}")
