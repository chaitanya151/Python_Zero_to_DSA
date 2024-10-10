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