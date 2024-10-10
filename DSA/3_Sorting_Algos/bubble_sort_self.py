arr = [5, 7, 8, 1, 9, 3, 2]

# Worst case - O(N^2)
n = len(arr)
print(f"length of an array: {n}")

for i in range(n - 2, -1, -1):
    for j in range(0, i + 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)

# Best case -> sorted array
n = len(arr)
print(f"length of an array: {n}")

for i in range(n - 2, -1, -1):
    swap = False
    for j in range(0, i + 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swap = True
    if swap == False:
        break

# sorting in decending order
arr = [5, 15, 10, 76]

n = len(arr)
print(n)
for i in range(n - 2, -1, -1):
    swap = False
    for j in range(0, i + 1):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swap = True
    if swap == False:
        break
print(arr)

# GPT code
arr = [10, 5, 7, 8]

n = len(arr)
print("Length of array:", n)

# Correct the range in the outer loop
for i in range(n - 1, 0, -1):
    swap = False
    for j in range(0, i):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swap = True
    if not swap:
        break

print("Sorted array in descending order:", arr)
