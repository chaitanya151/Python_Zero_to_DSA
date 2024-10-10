def reverse_array(arr, start, end):
    if start > end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse_array(arr, start + 1, end - 1)


# using single pointer


def rev_array(arr, index):
    n = len(arr)
    if index == n // 2:
        print(arr)
        return
    arr[index], arr[n - 1 - index] = arr[n - 1 - index], arr[index]
    rev_array(arr, index + 1)


if __name__ == "__main__":
    arr = [55, 63, 21, 32, 67, 91]
    n = len(arr)
    reverse_array(arr, 2, n - 1)
    print(arr)
    rev_array(arr, 0)
    print(arr)
